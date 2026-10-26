import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), "
        "trash the terminal and open a new one. If you have the extension "
        "'Python Test Explorer for Visual Studio Code', uninstall it and run tests "
        "from the 'Python Tests' tree."
    ) from None

from src.legendary_hunt import generation_count, legendary_dragons, hidden_legends

REAL = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "pokemon.csv")

MINI = pd.DataFrame({
    "Name":       ["Sparky", "Wyrm", "Drako", "Titan", "Bramble", "Colossus", "Glimmer"],
    "Type 1":     ["Electric", "Dragon", "Dragon", "Rock", "Grass", "Steel", "Dragon"],
    "Generation": [1, 1, 3, 3, 5, 5, 5],
    "HP":         [50, 100, 90, 110, 60, 100, 100],
    "Attack":     [60, 120, 110, 120, 50, 100, 100],
    "Defense":    [40, 100, 100, 130, 60, 100, 100],
    "Sp. Atk":    [70, 110, 100, 90, 55, 100, 100],
    "Sp. Def":    [50, 100, 100, 100, 60, 100, 100],
    "Speed":      [90, 90, 120, 70, 45, 100, 100],
    "Legendary":  [False, True, False, True, False, False, True],
})

NOT_A_TABLE = "should return a DataFrame (the filtered table), not a number"


class TestGenerationCount(unittest.TestCase):
    def test_real_pokedex(self):
        self.assertEqual(generation_count(REAL.copy()), 6,
                         msg="should be the number of different generations in the real Pokédex")

    def test_small_table(self):
        self.assertEqual(generation_count(MINI.copy()), 3,
                         msg="should be the number of different generations in the small table "
                             "(it has generations 1, 3 and 5)")


class TestLegendaryDragons(unittest.TestCase):
    def test_real_pokedex(self):
        result = legendary_dragons(REAL.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        expected = [
            "Latias", "LatiasMega Latias", "Latios", "LatiosMega Latios",
            "Rayquaza", "RayquazaMega Rayquaza", "Reshiram", "Zekrom",
            "Kyurem", "KyuremBlack Kyurem", "KyuremWhite Kyurem", "Zygarde50% Forme",
        ]
        self.assertEqual(list(result["Name"]), expected,
                         msg="should be the Pokémon in the real Pokédex whose Type 1 is Dragon "
                             "and that are legendary")

    def test_small_table(self):
        result = legendary_dragons(MINI.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(list(result["Name"]), ["Wyrm", "Glimmer"],
                         msg="should only include Pokémon that are BOTH Dragon type AND legendary")


class TestHiddenLegends(unittest.TestCase):
    def test_real_pokedex(self):
        result = hidden_legends(REAL.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertIn("Total", result.columns, msg="should have a Total column")
        expected_names = [
            "VenusaurMega Venusaur", "CharizardMega Charizard X", "CharizardMega Charizard Y",
            "BlastoiseMega Blastoise", "GyaradosMega Gyarados", "AerodactylMega Aerodactyl",
            "AmpharosMega Ampharos", "SteelixMega Steelix", "TyranitarMega Tyranitar",
            "SceptileMega Sceptile", "BlazikenMega Blaziken", "SwampertMega Swampert",
            "GardevoirMega Gardevoir", "Slaking", "AggronMega Aggron",
            "SalamenceMega Salamence", "MetagrossMega Metagross", "GarchompMega Garchomp",
            "LucarioMega Lucario", "GalladeMega Gallade",
        ]
        expected_totals = [625, 634, 634, 630, 640, 615, 610, 610, 700, 630,
                           630, 635, 618, 670, 630, 700, 700, 700, 625, 618]
        self.assertEqual(list(result["Name"]), expected_names,
                         msg="should be every non-legendary Pokémon with a Total over 600. "
                             "'over 600' means more than 600 — Pokémon with exactly 600 "
                             "shouldn't be included")
        self.assertEqual(list(result["Total"]), expected_totals,
                         msg="Total should be HP + Attack + Defense + Sp. Atk + Sp. Def + Speed")

    def test_small_table(self):
        result = hidden_legends(MINI.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertIn("Total", result.columns, msg="should have a Total column")
        self.assertEqual(list(result["Name"]), ["Drako"],
                         msg="should be every non-legendary Pokémon in the small table "
                             "with a Total over 600")
        self.assertEqual(list(result["Total"]), [620],
                         msg="Total should be HP + Attack + Defense + Sp. Atk + Sp. Def + Speed")


if __name__ == "__main__":
    unittest.main()
