# Legendary Hunt

Answer three questions about legendary Pokémon, one function each.

## The questions

All three functions are in `src/legendary_hunt.py`.

1. **How many generations of Pokémon are there?** `generation_count(df)` returns the number of different generations.
2. **Which Pokémon are legendary Dragons?** `legendary_dragons(df)` returns a DataFrame of the Pokémon whose Type 1 is Dragon and that are legendary.
3. **Which Pokémon are as strong as legends but aren't legendary?** `hidden_legends(df)` adds a Total column (HP + Attack + Defense + Sp. Atk + Sp. Def + Speed), then returns a DataFrame of every non-legendary Pokémon with a Total over 600.

Questions 2 and 3 return a table (a DataFrame), not a number. Run the file to see your tables.

Every function must work on any Pokédex table with these columns; the tests also use a small practice table.

## How to run

- See your findings: `python src/legendary_hunt.py`
- Run the tests: `python -m unittest discover` (or use the "Python Tests" tree in the Testing panel)

## If tests won't run

- **"No module named pandas"**: select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), then trash the terminal and open a new one.
- If "Python Test Explorer for Visual Studio Code" is installed, uninstall it; it ignores your interpreter choice.
- Open the assignment folder itself (File → Open Folder), not a folder above it.
- Windows: if conda won't activate in the terminal, run `conda init powershell` once in Anaconda Prompt and restart VS Code.
