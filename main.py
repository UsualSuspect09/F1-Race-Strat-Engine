from src.predict import predict_stint_length
from src.simulate import get_valid_strategies, simulate_strategy, compare_strategies

result = simulate_strategy('Monaco Grand Prix', ['Soft', 'Medium'], 78)
print(result)
