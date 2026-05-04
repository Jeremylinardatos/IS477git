import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("clean_data/full_dataset.csv")

# figure 1
plt.figure(figsize=(10, 6))

plt.scatter(
    x=df['AT'],
    y=df['hit_distance_sc'],
    c=df['launch_speed']
)

plt.colorbar(label="Exit Velocity")

plt.xlabel('Temperature (°C)')
plt.ylabel('Hit Distance')
plt.title('Hit Distance vs. Temperature')

plt.savefig("figures/hit-distance-vs-temp.jpg")

# figure 2
plt.figure(figsize=(10, 6))

plt.scatter(
    x=df['WD'],
    y=df['hit_distance_sc'],
    c=df['launch_angle'],
    cmap='magma'
)

plt.colorbar(label="Launch Angle")

plt.xlabel('Wind Direction')
plt.ylabel('Hit Distance')
plt.title('Hit Distance vs. Wind Direction')

plt.savefig("figures/hit-distance-vs-wind.jpg")

# figure 3

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)

plt.title("Correlation Heatmap")
plt.savefig("figures/corr_heatmap.jpg")