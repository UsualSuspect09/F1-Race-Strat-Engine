from src.predict import predict_stint_length
from src.utils import get_pit_window
from src.config import RACE_LAPS
import pandas as pd
# Simulates a single compound sequence for a given GP.
# Predicts each stint sequentially and enforces the lap budget.

from itertools import product
 
COMPOUNDS = ['SOFT', 'MEDIUM', 'HARD']
 
def get_valid_strategies(n_stops=1):
    """
    Returns a list of compound sequences for the given number of stops.
    Each sequence is a list of compounds, one per stint.
    
    n_stops=1 → 2 stints, n_stops=2 → 3 stints
    
    Enforces the F1 rule: at least 2 distinct compounds must be used.
    """
    n_stints = n_stops + 1
    all_sequences = list(product(COMPOUNDS, repeat=n_stints))
    
    # Filter: must use at least 2 different compounds
    valid = [seq for seq in all_sequences if len(set(seq)) >= 2]
    return valid
 
 
# Preview
# print("1-stop strategies:", len(get_valid_strategies(1)))
# print("2-stop strategies:", len(get_valid_strategies(2)))
# print()
# print("Sample 1-stop strategies:")
# for s in get_valid_strategies(1):
#     print(" →", " → ".join(s))

 
def simulate_strategy(gp, compound_sequence, total_laps):
    """
    Simulates a full race strategy for a given GP and compound sequence.
    
    Parameters:
        gp (str): Grand Prix name (must match model training data)
        compound_sequence (list): e.g. ['MEDIUM', 'HARD'] for a 1-stop
        total_laps (int): Total race laps for the GP
    
    Returns:
        dict with stint breakdown, predicted laps per stint, and validity flag
    """
    stints = []
    laps_used = 0
 
    for i, compound in enumerate(compound_sequence):
        stint_number = i + 1
        remaining_laps = total_laps - laps_used
        is_last_stint = (i == len(compound_sequence) - 1)
 
        if is_last_stint:
            # Final stint absorbs whatever laps remain
            predicted = remaining_laps
        else:
            predicted = predict_stint_length(gp, compound, stint_number)
            # Clamp: can't predict more than laps remaining (leave at least 1 lap for last stint)
            predicted = int(round(predicted))
            predicted = max(predicted, 5)  # must be at least 5 laps
            predicted = min(predicted, remaining_laps - (len(compound_sequence) - stint_number))
 
        laps_used += predicted
 
        stints.append({
            'Stint': stint_number,
            'Compound': compound,
            'PredictedLaps': round(predicted, 1),
            'PitWindow': get_pit_window(predicted)
        })
 
    total_predicted = sum(s['PredictedLaps'] for s in stints)
    budget_ok = abs(total_predicted - total_laps) <= 0.5  # within rounding
 
    return {
        'GP': gp,
        'Strategy': ' → '.join(compound_sequence),
        'Stints': stints,
        'TotalPredictedLaps': round(total_predicted, 1),
        'RaceLaps': total_laps,
        'BudgetValid': budget_ok
    }


def compare_strategies(gp, n_stops_list=[1, 2]):
    """
    Compares all valid strategies for a given GP across 1-stop and 2-stop.
    
    Returns a DataFrame with one row per strategy, sorted by
    how evenly the laps are distributed across stints (proxy for feasibility).
    """
    total_laps = RACE_LAPS.get(gp)
    if total_laps is None:
        raise ValueError(f"GP '{gp}' not found in RACE_LAPS. Check spelling.")
 
    rows = []
 
    for n_stops in n_stops_list:
        sequences = get_valid_strategies(n_stops)
        for seq in sequences:
            result = simulate_strategy(gp, seq, total_laps)
 
            # Compute stint balance: std dev of predicted stint lengths
            # Lower = more evenly distributed race (generally preferred strategically)
            stint_lengths = [s['PredictedLaps'] for s in result['Stints']]
            import numpy as np
            balance_score = round(np.std(stint_lengths), 2)
 
            stint_detail = ' | '.join(
                f"S{s['Stint']} {s['Compound']} ({s['PredictedLaps']} laps)"
                for s in result['Stints']
            )
 
            rows.append({
                'Strategy': result['Strategy'],
                'Stops': n_stops,
                'StintDetail': stint_detail,
                'TotalLaps': result['TotalPredictedLaps'],
                'BalanceScore': balance_score,  # lower = more even
            })
 
    df = pd.DataFrame(rows).sort_values(by='BalanceScore')
    return df
 
