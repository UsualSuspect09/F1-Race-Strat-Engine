import pandas as pd
import fastf1
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler

# Enable F1_cache to speed up data retrieval
fastf1.Cache.enable_cache("f1_cache")

def time_to_seconds(x):

    if pd.isna(x):
        return None

    return x.total_seconds()

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

driver_df_2024 = collect_driver_data(2024)

print(driver_df_2024.shape)

print(driver_df_2024.head())

driver_df_2024.to_csv(
    "datasets/raw_driver_2024.csv",
    index=False
)