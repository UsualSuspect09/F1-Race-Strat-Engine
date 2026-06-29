Model: Ridge Regression
Dataset: 2023 only
Stints: ~1198
MAE: 5.95

Model: Ridge Regression
Dataset: 2023 + 2024
Stints: 2427
MAE: 6.28

Model: Ridge Regression
Combined Dataset MAE with weather features: 6.143372292968852
Total stints: 2427


Best Ridge MAE (All Races):
6.143

Best Ridge MAE (Dry-Only):
5.830

Ridge Frozen Features:
GP
Compound
Stint
GP_Stint
Compound_Stint
Season
AirTemp
TrackTemp
RaceProgress

Dataset:
Dry-only

Model:
Ridge

MAE:
~5.68

Phase 2B.7
XGBoost Baseline

Train MAE: 3.89
Test MAE: 4.43

Result:
Strong improvement over Ridge.
No obvious signs of severe overfitting.


Model V2:
GP only
Test MAE = 3.6645

Model V3:
GP + CircuitType + TrackLength
Test MAE = 3.5536

XGBoost Stint Predictor V1
--------------------------------
Train MAE : 1.81
Test MAE  : 3.55
5-Fold MAE: 3.71 ± 0.12 laps