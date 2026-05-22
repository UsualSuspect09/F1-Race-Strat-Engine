import pandas as pd
import fastf1
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler

# Enable F1_cache to speed up data retrieval
fastf1.Cache.enable_cache("f1_cache")

def time_to_seconds(x):

    if pd.isna(x):
        return None

    try:
        return pd.to_timedelta(x).total_seconds()

    except:
        return None


def collect_driver_data(year):

    all_laps = []

    schedule = fastf1.get_event_schedule(
        year,
        include_testing=False
    )

    for rnd, row in tqdm(
        schedule.iterrows(),
        total=len(schedule),
        desc=f"Collecting {year} race data"
    ):

        try:

            event = fastf1.get_event(year, rnd)

            session = event.get_session("R")

            session.load()

            laps = session.laps.copy()

            # metadata
            laps["RoundNumber"] = rnd
            laps["GP"] = event.EventName
            laps["Session"] = "R"
            laps["Date"] = event.EventDate

            all_laps.append(laps)

            print(f"Loaded {event.EventName}")

        except Exception as e:

            print(f"Skipped round {rnd}: {e}")

    driver_df = pd.concat(
        all_laps,
        ignore_index=True
    )

    return driver_df

# driver_df_2024 = collect_driver_data(2024)

# print(driver_df_2024.shape)

# print(driver_df_2024.head())

# driver_df_2024.to_csv(
#     "datasets/raw_driver_2024.csv",
#     index=False
# )

def clean_driver_data(driver_df):

    # Make copy
    cleaned_df = driver_df.copy()

    # -------------------------
    # Convert time columns
    # -------------------------

    time_cols = [
        'LapTime',
        'Sector1Time',
        'Sector2Time',
        'Sector3Time'
    ]

    for col in time_cols:

        cleaned_df[col] = cleaned_df[col].apply(
            time_to_seconds
        )

    # -------------------------
    # Drop missing LapTime/Compound
    # -------------------------

    before_drop = cleaned_df.shape[0]

    cleaned_df = cleaned_df.dropna(
        subset=['LapTime', 'Compound']
    )

    print(
        f"Dropped {before_drop - cleaned_df.shape[0]} rows "
        f"with missing LapTime/Compound"
    )

    # -------------------------
    # Handle TyreLife
    # -------------------------

    missing_tyre = cleaned_df['TyreLife'].isna().sum()

    cleaned_df['TyreLife'] = (
        cleaned_df['TyreLife']
        .fillna(0)
        .astype(int)
    )

    print(
        f"Filled {missing_tyre} missing TyreLife values with 0"
    )

    # -------------------------
    # Handle FreshTyre
    # -------------------------

    missing_fresh = cleaned_df['FreshTyre'].isna().sum()

    cleaned_df['FreshTyre'] = (
        cleaned_df['FreshTyre']
        .fillna(False)
        .astype(int)
    )

    print(
        f"Filled {missing_fresh} missing FreshTyre values with False"
    )

    # -------------------------
    # Remove outlier laps
    # -------------------------

    median_lap = cleaned_df['LapTime'].median()

    before_outlier = cleaned_df.shape[0]

    cleaned_df = cleaned_df[
        cleaned_df['LapTime'] < 1.5 * median_lap
    ]

    print(
        f"Removed "
        f"{before_outlier - cleaned_df.shape[0]} outlier laps"
    )

    # -------------------------
    # Reset index
    # -------------------------

    cleaned_df = cleaned_df.reset_index(drop=True)

    return cleaned_df


driver_df_2024 = pd.read_csv("datasets/2024 Datasets/raw_driver_2024.csv")

# cleaned_df_2024 = clean_driver_data(driver_df_2024)

# cleaned_df_2024.to_csv("datasets/2024 Datasets/cleaned_driver_2024.csv", index=False)

# print("Data collection and cleaning complete!")

def collect_weather(year):

    all_weather = []

    schedule = fastf1.get_event_schedule(
        year,
        include_testing=False
    )

    sessions = ["FP1", "FP2", "FP3", "Q", "R"]

    for rnd, row in tqdm(
        schedule.iterrows(),
        total=len(schedule),
        desc=f"Collecting {year} weather"
    ):

        event = fastf1.get_event(year, rnd)

        for s in sessions:

            try:

                session = event.get_session(s)

                session.load()

                wd = session.weather_data.copy()

                wd["RoundNumber"] = rnd
                wd["EventName"] = event.EventName
                wd["Session"] = s
                wd["Date"] = event.EventDate

                all_weather.append(wd)

            except Exception as e:

                print(f"Skipped {rnd} {s}: {e}")

    weather_df = pd.concat(
        all_weather,
        ignore_index=True
    )

    weather_df.sort_values(
        ["RoundNumber", "Session", "Time"],
        inplace=True
    )

    return weather_df

weather_2024 = collect_weather(2024)

weather_2024.to_csv(
    "datasets/2024 Datasets/weather_2024.csv",
    index=False
)

print("Saved 2024 weather data")

