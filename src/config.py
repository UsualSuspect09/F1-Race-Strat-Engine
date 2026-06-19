# These are the official 2023 race lap counts.
# Used to enforce the lap budget constraint during simulation.
 
RACE_LAPS = {
    'Bahrain Grand Prix': 57,
    'Saudi Arabian Grand Prix': 50,
    'Australian Grand Prix': 58,
    'Azerbaijan Grand Prix': 51,
    'Miami Grand Prix': 57,
    'Monaco Grand Prix': 78,
    'Spanish Grand Prix': 66,
    'Canadian Grand Prix': 70,
    'Austrian Grand Prix': 71,
    'British Grand Prix': 52,
    'Hungarian Grand Prix': 70,
    'Belgian Grand Prix': 44,
    'Dutch Grand Prix': 72,
    'Italian Grand Prix': 51,
    'Singapore Grand Prix': 62,
    'Japanese Grand Prix': 53,
    'Qatar Grand Prix': 57,
    'United States Grand Prix': 56,
    'Mexico City Grand Prix': 71,
    'São Paulo Grand Prix': 71,
    'Las Vegas Grand Prix': 50,
    'Abu Dhabi Grand Prix': 58,
}

# Given a predicted stint length, returns a pit window based on the initial MAE of the model. 
# The window is defined as predicted_laps ± WINDOW_MARGIN, clamped

WINDOW_MARGIN = 6



import pandas as pd

# -----------------------------------
# Load Master Stint Datasets
# -----------------------------------
stint_2023 = pd.read_csv(
    "C:/Users/VANSH/Formula1/datasets/2023/master_stint_2023_v2.csv"
)

stint_2024 = pd.read_csv(
    "C:/Users/VANSH/Formula1/datasets/2024/master_stint_2024_v2.csv"
)

# -----------------------------------
# Combine Seasons
# -----------------------------------

combined_df = pd.concat(
    [stint_2023, stint_2024],
    ignore_index=True
)

# -----------------------------------
# Calculate GP Weather Averages
# -----------------------------------

weather_table = (
    combined_df
    .groupby("GP")[
        ["AirTemp", "TrackTemp"]
    ]
    .mean()
    .round(1)
)

# -----------------------------------
# Convert To Dictionaries
# -----------------------------------

avg_air_temp = (
    weather_table["AirTemp"]
    .to_dict()
)

avg_track_temp = (
    weather_table["TrackTemp"]
    .to_dict()
)

# -----------------------------------
# Save To Python Config File
# -----------------------------------

with open(
    "weather_config.py",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "# Auto-generated weather configuration\n\n"
    )

    file.write(
        f"AVG_AIR_TEMP = {avg_air_temp}\n\n"
    )

    file.write(
        f"AVG_TRACK_TEMP = {avg_track_temp}\n"
    )

print(
    "weather_config.py created successfully."
)

print(
    "\nTotal GPs:",
    len(avg_air_temp)
)