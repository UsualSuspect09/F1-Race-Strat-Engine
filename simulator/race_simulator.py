import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator.stint_predictor import (
    StintPredictor
)


class RaceSimulator:

    def __init__(self):

        self.predictor = (
            StintPredictor()
        )

    def simulate_strategy(
        self,
        strategy,
        race_context
    ):

        completed_laps = 0

        predicted_stints = []

        race_progresses = []

        race_laps = (
            race_context["race_laps"]
        )

        # Predict all stints except the final one
        for compound in strategy[:-1]:

            race_progress = (
                completed_laps /
                race_laps
            )

            race_progresses.append(
                round(
                    race_progress,
                    3
                )
            )

            stint_length = (
                self.predictor
                .predict_stint_length(
                    compound=compound,
                    GP=race_context[
                        "gp_name"
                    ],
                    air_temp=race_context[
                        "air_temp"
                    ],
                    track_temp=race_context[
                        "track_temp"
                    ],
                    season=race_context[
                        "season"
                    ],
                    race_progress=race_progress,
                    circuit_type=race_context[
                        "circuit_type"
                    ],
                    track_length=race_context[
                        "track_length"
                    ],
                    track_abrasiveness=race_context[
                        "track_abrasiveness"
                    ],
                    average_corner_speed=race_context[
                        "average_corner_speed"
                    ]
                )
            )
            stint_length = round(
                stint_length
            )

            predicted_stints.append(
                
                    stint_length
            )
                 

            completed_laps += (
                    stint_length
                )

        # Final stint absorbs the remaining laps
        final_compound = (
            strategy[-1]
        )

        race_progress = (
            completed_laps /
            race_laps
        )

        race_progresses.append(
            round(
                race_progress,
                3
            )
        )

        final_stint = round(
            race_laps -
            completed_laps,
            1
        )

        predicted_stints.append(
            final_stint
        )

        total_laps = round(
            sum(
                predicted_stints
            ),
            1
        )

        coverage_margin = round(
            total_laps - race_laps,
            1
        )

        return {

            "strategy":
                strategy,

            "race_progresses":
                race_progresses,

            "predicted_stints":
                predicted_stints,

            "total_laps":
                total_laps,

            "race_laps":
                race_laps,

            "coverage_margin":
                coverage_margin,

            "pit_stops":
                len(strategy) - 1,

            "valid":
                total_laps >= race_laps,

            "final_compound":
                final_compound,

            "circuit_type":
                race_context["circuit_type"]

        }