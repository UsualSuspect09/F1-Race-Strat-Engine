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

