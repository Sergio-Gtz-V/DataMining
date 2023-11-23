import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_database.csv')
output_dir = 'img/graphs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

"""
def records_per_season_graph(df):
    season_count = df['SEASON'].value_counts()
    plt.bar(season_count.index, season_count.values)
    plt.xlabel('Season')
    plt.ylabel('# of Records')
    plt.title('Records per season')
    plt.xticks(np.arange(min(season_count.index), max(season_count.index) + 1, 1), rotation = 90)
    plt.savefig(os.path.join(output_dir, 'records_per_season_graph'))
    plt.show()


def points_avg_by_team_by_season(df):
    season_team_avg = df.groupby(['SEASON', 'HOME_TEAM'])['PTS_home'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    for team in season_team_avg['HOME_TEAM'].unique():
        team_data = season_team_avg[season_team_avg['HOME_TEAM'] == team]
        plt.plot(team_data['SEASON'], team_data['PTS_home'], label=team, marker='o')
    plt.xlabel('Season')
    plt.ylabel('Average Points')
    plt.title('Average Points per Season per Team')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'points_avg_by_team_by_season'))
    plt.show() 
"""
# Calculate total points scored by all teams as away teams for each season
away_team_total_points = df.groupby(['SEASON', 'AWAY_TEAM'])['PTS_away'].sum().reset_index()

# Calculate total points scored by all teams as away teams over all seasons
total_points_all_time = away_team_total_points.groupby('AWAY_TEAM')['PTS_away'].sum().reset_index()

total_points_all_time_sorted = total_points_all_time.sort_values(by='PTS_away', ascending=False)

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(total_points_all_time_sorted['AWAY_TEAM'], total_points_all_time_sorted['PTS_away'], color='skyblue')
plt.xlabel('Team')
plt.ylabel('Total Points (Away Games)')
plt.title('Total Points Scored by All Teams (Away Games) All Time Sorted best to worse')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Points_acc_as_away_sorted'))
plt.show()
#records_per_season_graph(df)
#points_avg_by_team_by_season(df)
