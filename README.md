# Useless champions

A program to disenchant League of Legends useless champion fragments.

> [!IMPORTANT]
> Since the current masteries updates, any champion fragment that is not upgradeable is useless.

![A useless champion example](https://images.contentstack.io/v3/assets/blt187521ff0727be24/blt21051e981c6ebb3f/60ee1226730ed71c59413b01/sona-color-splash.jpg)

## Requirements

- [Python](https://www.python.org/downloads/) >= 3.10.12
- [League of Legends](https://www.leagueoflegends.com/)

## How to use

1. Optionally set a virtual environment `python -m venv .venv` and activate it
2. Install the dependencies by running `pip install -r requirements.txt`
3. Log in League of Legends
4. Run `python main.py` to disenchant all useless champions, and also upgrade upgradeable champions

## Options

- `-u` or `--upgrade` alone will search and upgrade all upgradeable champions. You can optionally specify champions as arguments with the format: `aatrox ahri`
- `-d` or `--disenchant` alone **will disenchant all champion fragments**. To specify champions as arguments use this format instead `aatrox 1 ahri 2`

## Test

To test the program run `pytest`.