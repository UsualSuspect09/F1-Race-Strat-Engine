def generate_strategies():

    strategies = [

        ["SOFT", "HARD"],

        ["MEDIUM", "HARD"],

        ["SOFT", "MEDIUM", "HARD"],

        ["MEDIUM", "SOFT", "HARD"],

        ["HARD", "MEDIUM"]
    ]

    return strategies


if __name__ == "__main__":
    strategies = generate_strategies()
    print("Generated Strategies:")
    for strategy in strategies:
        print(f" - {strategy}")