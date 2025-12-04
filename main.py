import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

api = KaggleApi()
api.authenticate()  

api.dataset_download_files("ggtejas/tmdb-imdb-merged-movies-dataset", path='.', unzip=True)
os.rename('TMDB  IMDB Movies Dataset.csv', 'tmdb.csv')


df = pd.read_csv("tmdb.csv")

df = df.rename(columns={
    "title": "title",
    "overview": "description",
    "vote_average": "rating",
    "backdrop_path": "backdrop_path"
})

if "release_date" in df.columns:
    df["year"] = pd.to_datetime(df["release_date"], errors='coerce').dt.year
else:
    df["year"] = None

df = df[["title", "description", "rating", "year", "backdrop_path"]]

df.to_json("movies.json", orient="records", force_ascii=False, indent=4)

print("✔ movies.json created successfully!")
