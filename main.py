import api
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="useless-champions",
        description="Disenchant League of Legends Hextech useless champion fragments",
        epilog="See source code at: https://github.com/brunomisto/useless-champions"
    )

    parser.add_argument(
        "-d", "--disenchant",
        dest="disenchant", 
        nargs="*",
        type=str
    )

    parser.add_argument(
        "-u", "--upgrade",
        dest="upgrade",
        nargs="*",
        type=str,
    )

    args = parser.parse_args()

    connection = api.LCU_Connection()

    if args.disenchant == None and args.upgrade == None:
        useless = connection.get_useless_champions()
        connection.disenchant_champions(useless)

        upgradeable = connection.get_upgradeable_champions()
        connection.upgrade_champions(upgradeable)
        return

    if args.disenchant == None:
        disenchant = []
    elif len(args.disenchant) == 0:
        disenchant = parse_all_champions(connection.champions)
        print("WARNING: SELECTED ALL CHAMPION FRAGMENTS")
    else:
        disenchant = parse_disenchant_arguments(connection.champions, args.disenchant)
    
    if args.upgrade == None:
        upgrade = []
    elif len(args.upgrade) == 0:
        upgrade = connection.get_upgradeable_champions()
    else:
        upgrade = parse_upgrade_arguments(connection.champions, args.upgrade)

    connection.disenchant_champions(disenchant)
    connection.upgrade_champions(upgrade)


def parse_champion_name(champions, name):
    for champion in champions:
        if champion["itemDesc"].lower() == name.lower():
            return champion["lootId"]
    print(f"{name} was not found")


def parse_all_champions(champions):
    champion_dict = {}

    for champion in champions:
        champion_dict[champion["lootId"]] = champion["count"]

    return champion_dict


def parse_disenchant_arguments(champions, champion_arguments: list):
    tupled_champions = list(
        zip(champion_arguments[0::2], champion_arguments[1::2])
    )
    unparsed_champion_dict = dict(tupled_champions)

    champion_dict = {}

    for champion in unparsed_champion_dict:
        loot_id = parse_champion_name(champions, champion)

        if loot_id:
            repeat = unparsed_champion_dict[champion]
            champion_dict[loot_id] = repeat
    
    return champion_dict


def parse_upgrade_arguments(champions, champion_arguments: list):
    champion_dict = {}

    for champion in champion_arguments:
        loot_id = parse_champion_name(champions, champion)

        if loot_id:
            champion_dict[loot_id] = 1
    
    return champion_dict


if __name__ == "__main__":
    main()