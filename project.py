import api
import sys


def main():
    connection = api.LCU_Connection()

    if len(sys.argv) == 1:
        useless = get_useless(connection)
        disenchant_champions(connection, useless)

        upgradeable = get_upgradeable(connection)
        upgrade_champions(connection, upgradeable)
        return

    if len(sys.argv) == 2:
        champion_dict = parse_champions(connection)
        print(champion_dict)
    elif len(sys.argv) % 2 == 0:
        champion_dict = parse_champion_arguments(connection, sys.argv[2:])
    else:
        sys.exit("Not enough arguments.")

    if sys.argv[1] in ("-d", "--disenchant"):
        disenchant_champions(connection, champion_dict)
        return

    if sys.argv[1] in ("-u", "--upgrade"):
        upgrade_champions(connection, champion_dict)
        return
    
    sys.exit("Usage: python project.py [-u [champion count...]] [-d [champion count...]]")
    

def parse_champion_arguments(connection: api.LCU_Connection, champion_arguments):
    tupled_champions = list(
        zip(champion_arguments[0::2], champion_arguments[1::2])
    )
    unparsed_champion_dict = dict(tupled_champions)

    champion_dict = {}

    for champion in unparsed_champion_dict:
        loot_id = parse_champion_name(connection, champion)

        if loot_id:
            repeat = unparsed_champion_dict[champion]
            champion_dict[loot_id] = repeat
    
    return champion_dict
    

def parse_champions(connection: api.LCU_Connection):
    champion_dict = {}

    for champion in connection.champions:
        champion_dict[champion["lootId"]] = champion["count"]

    return champion_dict
    

def parse_champion_name(connection: api.LCU_Connection, name):
    for champion in connection.champions:
        if champion["itemDesc"].lower() == name.lower():
            return champion["lootId"]
    print(f"{name} was not found")


def get_useless(connection: api.LCU_Connection):
    return connection.get_useless_champions()


def disenchant_champions(connection: api.LCU_Connection, champion_dict):
    return connection.disenchant_champions(champion_dict)


def get_upgradeable(connection: api.LCU_Connection):
    return connection.get_upgradeable_champions()


def upgrade_champions(connection: api.LCU_Connection, champion_dict):
    return connection.upgrade_champions(champion_dict)


if __name__ == "__main__":
    main()