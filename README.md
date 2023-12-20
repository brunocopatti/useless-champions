# useless-champions
A program to disenchant League of Legends useless champion fragments.

![A useless champion example](https://images.contentstack.io/v3/assets/blt187521ff0727be24/blt21051e981c6ebb3f/60ee1226730ed71c59413b01/sona-color-splash.jpg)

## Requirements
- [Python](https://www.python.org/downloads/)
- [League of Legends](https://www.leagueoflegends.com/)
- League of Legends account

## How to use
1. Install the dependencies by running `pip install -r requirements.txt`
2. Run and login in League of Legends
3. Run `python main.py` if you want to disenchant all useless champions, and also upgrade available champions.

## Options
- `-u` or `--upgrade` alone will search and upgrade all upgradeable champions. You can specify which champions you want with arguments like `-u aatrox ahri`.
- `-d` or `--disenchant` alone **will disenchant all champion fragments**. You can specify champions with the format `-d aatrox 1 ahri 2`. (**It needs to be like this**)
