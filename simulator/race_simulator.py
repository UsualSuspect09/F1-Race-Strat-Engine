# from simulator.stint_predictor import (
#     StintPredictor
# )


# class RaceSimulator:

#     def __init__(self):

#         self.predictor = (
#             StintPredictor()
#         )

#     def simulate_strategy(
#         self,
#         strategy,
#         race_context
#     ):

#         completed_laps = 0

#         predicted_stints = []

#         race_laps = (
#             race_context["race_laps"]
#         )

#         for compound in strategy:

#             race_progress = (
#                 completed_laps /
#                 race_laps
#             )

#             stint_length = (
#                 self.predictor
#                 .predict_stint_length(
#                     compound=compound,
#                     air_temp=race_context[
#                         "air_temp"
#                     ],
#                     track_temp=race_context[
#                         "track_temp"
#                     ],
#                     season=race_context[
#                         "season"
#                     ],
#                     race_progress=race_progress
#                 )
#             )

#             predicted_stints.append(
#                 stint_length
#             )

#             completed_laps += (
#                 round(stint_length)
#             )

#         total_laps = (
#             sum(predicted_stints)
#         )

#         return {

#             "strategy": strategy,

#             "predicted_stints":
#                 predicted_stints,

#             "total_laps":
#                 round(total_laps, 1),

#             "pit_stops":
#                 len(strategy) - 1,

#             "valid":
#                 total_laps >= race_laps

#         }

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

        # -------------------------
        # Initialize
        # -------------------------

        completed_laps = 0

        predicted_stints = []

        race_progresses = []

        race_laps = (
            race_context["race_laps"]
        )

        # -------------------------
        # Simulate Each Stint
        # -------------------------

        for compound in strategy:

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

        # -------------------------
        # Final Metrics
        # -------------------------

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