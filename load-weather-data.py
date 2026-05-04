import pandas as pd
import hashlib

# read in data downloaded from website
weather = pd.read_csv("raw_data/weather.avg", sep=r"\s+", skiprows=11)

# verify integrity of data using SHA256
weather_clean = (
    weather
    .sort_values(by=list(weather.columns))
    .reset_index(drop=True)
)

weather_clean = weather_clean[sorted(weather_clean.columns)]

weather_csv_bytes = weather_clean.to_csv(index=False).encode('utf-8')
weather_hash_val = hashlib.sha256(weather_csv_bytes).hexdigest()

with open("hashes/weather_sha.txt", "r") as f:
    weather_expected_hash = f.read().strip()

assert weather_hash_val == weather_expected_hash, (
    f"Hash mismatch!\nExpected:{weather_expected_hash}\nGot:{weather_hash_val}"
)

# drop unnecessary columns and create date column
weather = weather.drop(columns=['n'])
weather['date'] = pd.to_datetime('2025-01-01') + pd.to_timedelta(weather['DOY'] - 1, unit='D')

weather.to_csv('clean_data/weather.csv', index=False)