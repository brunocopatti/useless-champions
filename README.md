# useless-champions

A program to disenchant League of Legends useless champion fragments.

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