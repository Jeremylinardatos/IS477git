
import pandas as pd
import hashlib
from pybaseball import statcast, batting_stats_bref, playerid_reverse_lookup

#---------------#
#   Dataset 1   #
#---------------#

# get statcast data from pybaseball
sc = statcast(start_dt="2025-01-01", end_dt="2025-12-31", team="CHC")

# verify integrity of dataset using SHA256
sc_clean = (
    sc
    .sort_values(by=list(sc.columns))
    .reset_index(drop=True)
)

sc_clean = sc_clean[sorted(sc_clean.columns)]

sc_csv_bytes = sc_clean.to_csv(index=False).encode('utf-8')
sc_hash_val = hashlib.sha256(sc_csv_bytes).hexdigest()

with open("hashes/home_runs_sha.txt", "r") as f:
    sc_expected_hash = f.read().strip()

assert sc_hash_val == sc_expected_hash, (
    f"Hash mismatch!\nExpected:{sc_expected_hash}\nGot:{sc_hash_val}"
)

# filter to only home runs in Wrigley
hrs = sc[(sc['events'] == 'home_run') & (sc['home_team'] == 'CHC')]

# convert player ids to names
batter_names = playerid_reverse_lookup(hrs['batter'])
batter_names['full_name'] = batter_names["name_first"] + " " + batter_names["name_last"]
batter_names = batter_names[['key_mlbam', 'full_name']]

# merge names into hrs dataset
hrs = pd.merge(hrs, batter_names, how="inner", left_on="batter", right_on="key_mlbam")

# only get columns we need
hr_cols = ["game_date", "full_name", "launch_speed", "launch_angle", "hit_distance_sc", "pitch_type"]
hrs = hrs[hr_cols]

hrs.to_csv('clean_data/home_runs.csv', index=False)

#---------------#
#   Dataset 2   #
#---------------#

# load data from baseball reference
batting = batting_stats_bref(2025)

# verify integrity of dataset using SHA256
batting_clean = (
    batting
    .sort_values(by=list(batting.columns))
    .reset_index(drop=True)
)

batting_clean = batting_clean[sorted(batting_clean.columns)]

batting_csv_bytes = batting_clean.to_csv(index=False).encode('utf-8')
batting_hash_val = hashlib.sha256(batting_csv_bytes).hexdigest()

with open("hashes/batting_sha.txt", "r") as f:
    batting_expected_hash = f.read().strip()

assert batting_hash_val == batting_expected_hash, (
    f"Hash mismatch!\nExpected:{batting_expected_hash}\nGot:{batting_hash_val}"
)

# only get columns we need
batting_cols = ["Name", "OBP", "SLG"]
batting = batting[batting_cols]

batting.to_csv('clean_data/batting.csv', index=False)