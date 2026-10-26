import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/modengann/Data-sets/refs/heads/master/pokemon.csv"


def generation_count(df: pd.DataFrame) -> int:
    """How many generations of Pokémon are there? Return the number of different generations."""
    pass


def legendary_dragons(df: pd.DataFrame) -> pd.DataFrame:
    """Which Pokémon are legendary Dragons? Return a DataFrame of the Pokémon whose Type 1 is Dragon and that are legendary."""
    pass


def hidden_legends(df: pd.DataFrame) -> pd.DataFrame:
    """Which Pokémon are as strong as legends but aren't legendary?
    Add a Total column (HP + Attack + Defense + Sp. Atk + Sp. Def + Speed),
    then return a DataFrame of every non-legendary Pokémon with a Total over 600."""
    pass


def main():
    df = pd.read_csv(DATA_URL)
    print("Number of generations:", generation_count(df))
    print()
    print("Legendary Dragons:")
    print(legendary_dragons(df))
    print()
    print("Hidden legends:")
    print(hidden_legends(df))


if __name__ == "__main__":
    main()
