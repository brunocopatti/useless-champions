import api
import sys


def main():
    options = ("-d", "--disenchant", "-u", "--upgrade")
    if (len(sys.argv) != 1 and len(sys.argv) % 2 == 1) or (len(sys.argv) > 1 and sys.argv[1] not in options):
        sys.exit("Usage: python project.py [-u [champion count...]] [-d [champion count...]]")

    connection = api.LCU_Connection()

    if len(sys.argv) == 1:
        useless = connection.get_useless_champions()
        connection.disenchant_champions(useless)

        upgradeable = connection.get_upgradeable_champions()
        connection.upgrade_champions(upgradeable)
        return

    if len(sys.argv) == 2:
        champion_dict = parse_champions(connection.champions)
    else:
        champion_dict = parse_champion_arguments(sys.argv[2:])

    if sys.argv[1] in ("-d", "--disenchant"):
        connection.disenchant_champions(champion_dict)
        return

    if sys.argv[1] in ("-u", "--upgrade"):
        connection.upgrade_champions(champion_dict)
        return


def parse_champion_arguments(champions, champion_arguments: list):
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


def parse_champions(champions):
    champion_dict = {}

    for champion in champions:
        champion_dict[champion["lootId"]] = champion["count"]

    return champion_dict


def parse_champion_name(champions, name):
    for champion in champions:
        if champion["itemDesc"].lower() == name.lower():
            return champion["lootId"]
    print(f"{name} was not found")


if __name__ == "__main__":
    main()