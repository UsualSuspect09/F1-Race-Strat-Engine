def generate_strategies():

    strategies = [
    # One-stop

    ["SOFT", "HARD"],
    ["MEDIUM", "HARD"],
    ["HARD", "MEDIUM"],

    # Two-stop

    ["SOFT", "HARD", "HARD"],
    ["MEDIUM", "HARD", "HARD"],

    ["SOFT", "SOFT", "HARD"],
    ["MEDIUM", "MEDIUM", "HARD"],

    ["SOFT", "HARD", "SOFT"],
    ["MEDIUM", "HARD", "SOFT"],

    ["SOFT", "MEDIUM", "HARD"],
    ["MEDIUM", "SOFT", "HARD"]
]

    return strategies


if __name__ == "__main__":
    strategies = generate_strategies()
    print("Generated Strategies:")
    for strategy in strategies:
        print(f" - {strategy}")