from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


def open_file(path: str) -> str:
    content = ""
    with open(path, "r", encoding= "utf8") as f:
        content = f.readlines()
    return " ".join(content)



def open_dataframe_column(df: pd.DataFrame, column_name: str) -> str:
    
    if column_name not in df.columns:
        raise ValueError(f"La columna '{column_name}' no existe en el DataFrame.")

    content = " ".join(df[column_name].astype(str))

    return content


all_words = ""
frase = open_file("text.txt")
palabras = frase.rstrip().split(" ")
for arg in palabras:
    tokens = arg.split()
    all_words += " ".join(tokens) + " "

wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(all_words)

plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("img/graphs/textCloudFromTxt.png")
plt.close()



df = pd.read_csv("cleaned_database.csv")
palabras = open_dataframe_column(df, 'HOME_TEAM')
palabras = " ".join(palabras.split())
wordcloud2 = WordCloud(background_color="white", min_font_size=5).generate(palabras)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud2)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("img/graphs/textCloudFromDb.png")
plt.close()


