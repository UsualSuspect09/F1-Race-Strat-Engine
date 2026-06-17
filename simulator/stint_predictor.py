import joblib
import pandas as pd


class StintPredictor:

    def __init__(
        self,
        model_path="C:/Users/VANSH/Formula1/models/xgb_stint_model.pkl"
    ):

        self.model = joblib.load(
            model_path
        )

    def predict_stint_length(
        self,
        compound,
        air_temp,
        track_temp,
        season,
        race_progress,
        fresh_tyre=1,
        yellow_laps=0,
        sc_laps=0,
        vsc_laps=0,
        redflag_laps=0
    ):

        features = pd.DataFrame(
            {
                "Compound": [compound],
                "AirTemp": [air_temp],
                "TrackTemp": [track_temp],
                "Season": [season],
                "RaceProgress": [race_progress],
                "FreshTyre": [fresh_tyre],
                "YellowLaps": [yellow_laps],
                "SCLaps": [sc_laps],
                "VSCLaps": [vsc_laps],
                "RedFlagLaps": [redflag_laps]
            }
        )

        prediction = self.model.predict(
            features
        )[0]

        return round(
            float(prediction),
            1
        )