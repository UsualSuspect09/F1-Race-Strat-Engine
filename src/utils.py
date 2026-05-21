from src.config import WINDOW_MARGIN
def get_pit_window(predicted_laps):
    
    lower = max(1, int(round(predicted_laps - WINDOW_MARGIN)))
    upper = int(round(predicted_laps + WINDOW_MARGIN))
    
    return (lower, upper)