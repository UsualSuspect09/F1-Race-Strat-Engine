import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator.stint_predictor import (
    StintPredictor
)

predictor = StintPredictor()

prediction = (
    predictor.predict_stint_length(
        compound="MEDIUM",
        air_temp=28,
        track_temp=38,
        season=2024,
        race_progress=0
    )
)

print(
    "Predicted Stint Length:",
    prediction
)