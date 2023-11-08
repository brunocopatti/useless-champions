> [!WARNING]
> This project is being built, do not use it yet.

# useless-champions

A program to disenchant League of Legends useless champion fragments.

![A useless champion example](https://images.contentstack.io/v3/assets/blt187521ff0727be24/blt21051e981c6ebb3f/60ee1226730ed71c59413b01/sona-color-splash.jpg)

## Pseudocode

- Connect to LCU
- Get champion fragments data
- Get user mastery data
- For each champion
    - Keep x fragments if ...
        - 0 if mastery = 7
        - 1 if mastery = 6
        - 2 if owned
        - 3 if not owned
    - Prompt user for confirmation
- Get user blue essences
- For each champion
    - Check if is upgradeable
    - Prompt user for confirmation
- Exit

## TODO

- [X] Make essence relatable stuff in upgrade champions function