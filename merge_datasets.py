import pandas as pd

home_runs = pd.read_csv("clean_data/home_runs.csv")
batting = pd.read_csv("clean_data/batting.csv")
weather = pd.read_csv("clean_data/weather.csv")

# reformat name to lowercase for merging
batting['Name'] = batting['Name'].str.lower()

# merge baseball datasets
bb_merged = pd.merge(home_runs, batting, how='left', left_on='full_name', right_on='Name').drop(columns=['Name'])

# merge baseball and weather datasets
df = pd.merge(bb_merged, weather, how='left', left_on='game_date', right_on='date').drop(columns=['date'])

df.to_csv("clean_data/full_dataset.csv", index=False)