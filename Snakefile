rule all:
    input:
        "figures/corr_heatmap.jpg",
        "figures/hit-distance-vs-temp.jpg",
        "figures/hit-distance-vs-wind.jpg"

rule read_baseball:
    output:
        "clean_data/home_runs.csv",
        "clean_data/batting.csv"
    shell:
        "python3 load-baseball-data.py"

rule read_weather:
    input:
        "raw_data/weather.avg"
    output:
        "clean_data/weather.csv"
    shell:
        "python3 load-weather-data.py"

rule merge_datasets:
    input:
        "clean_data/home_runs.csv",
        "clean_data/batting.csv",
        "clean_data/weather.csv"
    output:
        "clean_data/full_dataset.csv"
    shell:
        "python3 merge_datasets.py"

rule visualizations:
    input:
        "clean_data/full_dataset.csv"
    output:
        "figures/corr_heatmap.jpg",
        "figures/hit-distance-vs-temp.jpg",
        "figures/hit-distance-vs-wind.jpg"
    shell:
        "python3 visualizations.py"