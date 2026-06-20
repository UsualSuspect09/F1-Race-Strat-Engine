import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import RACE_LAPS
from src.weather_config import (
    AVG_AIR_TEMP,
    AVG_TRACK_TEMP
)


def get_race_context(
    season,
    gp_name
):

    if gp_name not in RACE_LAPS:
        raise ValueError(
            f"{gp_name} not found in RACE_LAPS"
        )

    if gp_name not in AVG_AIR_TEMP:
        raise ValueError(
            f"{gp_name} not found in AVG_AIR_TEMP"
        )

    if gp_name not in AVG_TRACK_TEMP:
        raise ValueError(
            f"{gp_name} not found in AVG_TRACK_TEMP"
        )

    race_context = {

        "season": season,

        "gp_name": gp_name,

        "race_laps":
            RACE_LAPS[gp_name],

        "air_temp":
            AVG_AIR_TEMP[gp_name],

        "track_temp":
            AVG_TRACK_TEMP[gp_name]

    }

    return race_context




context = get_race_context(
    season=2024,
    gp_name="Bahrain Grand Prix"
)

print(context)