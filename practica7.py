import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode
from matplotlib.cm import get_cmap
from typing import List

def get_cmap(n, name="hsv"):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name."""
    return plt.cm.get_cmap(name, n)

# Assuming df is your DataFrame with the NBA teams' statistics
df = pd.read_csv('cleaned_database.csv')
output_dir = 'img/graphs'

def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neighbors(
    points: List[np.array], labels: np.array, input_data: List[np.array], k: int
):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest]).mode[0]
        for point_nearest in points_k_nearest
    ]

# Assuming 'PTS_home' and 'REB_home' are used for x and y coordinates
scatter_group_by("img/graphs/single_chart_scatter.png", df, "PTS_home", "REB_home", "HOME_TEAM")

list_t = [
    (np.array(tuples[5:7]), tuples[17])  # Assuming 'PTS_home' and 'REB_home' are used
    for tuples in df.itertuples(index=False, name=None)
]

points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

# Use specific points for k-nearest neighbors
kn = k_nearest_neighbors(
    points,
    labels,
    [np.array([100, 150]), np.array([90, 40]), np.array([110, 200])],
    5,
)
print(kn)

def scatter_group_by_separate_legends(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)

    fig, axs = plt.subplots(len(labels), 1, figsize=(8, 2 * len(labels)), sharex=True)

    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        axs[i].scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
        axs[i].legend(loc='upper right')

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()

# Assuming 'PTS_home' and 'REB_home' are used for x and y coordinates
scatter_group_by_separate_legends("img/graphs/scatter_separate.png", df, "PTS_home", "REB_home", "HOME_TEAM")
