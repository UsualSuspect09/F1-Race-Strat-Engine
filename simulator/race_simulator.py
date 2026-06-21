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

        for compound in strategy:

            # -------------------------
            # NORMALIZED RaceProgress
            # -------------------------

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

            print("-" * 50)
            print(
                f"Compound: {compound}"
            )
            print(
                f"Completed Laps: {completed_laps}"
            )
            print(
                f"Race Progress: {race_progress:.3f}"
            )

            stint_length = (
                self.predictor
                .predict_stint_length(
                    compound=compound,
                    air_temp=race_context[
                        "air_temp"
                    ],
                    track_temp=race_context[
                        "track_temp"
                    ],
                    season=race_context[
                        "season"
                    ],
                    race_progress=race_progress
                )
            )

            print(
                f"Predicted Stint: {stint_length}"
            )

            predicted_stints.append(
                round(
                    stint_length,
                    1
                )
            )

            completed_laps += (
                round(
                    stint_length
                )
            )

        total_laps = round(
            sum(
                predicted_stints
            ),
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

            "pit_stops":
                len(strategy) - 1,

            "valid":
                total_laps >= race_laps

        }