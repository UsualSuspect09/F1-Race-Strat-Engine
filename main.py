from src.predict import predict_stint_length
from src.simulate import get_valid_strategies, simulate_strategy, compare_strategies

result = simulate_strategy('British Grand Prix', ['Medium', 'Hard'], 37)
print(result)
