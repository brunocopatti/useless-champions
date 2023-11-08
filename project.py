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
    
    if not len(sys.argv) % 2 == 0 or len(sys.argv) < 4:
        sys.exit("Not enough arguments.")

    champion_arguments = sys.argv[2:]
    tupled_champions = list(
        zip(champion_arguments[0::2], champion_arguments[1::2])
    )
    unparsed_champion_dict = dict(tupled_champions)

    champion_dict = {}

    for champion in unparsed_champion_dict:
        loot_id = parse_champion_name(connection, champion)
        repeat = unparsed_champion_dict[champion]
        champion_dict[loot_id] = repeat

    print(champion_dict)

    if sys.argv[1] in ("-d", "--disenchant"):
        return

    if sys.argv[1] in ("-u", "--upgrade"):
        return
    

def parse_champion_name(connection: api.LCU_Connection, name):
    for champion in connection.champions:
        if champion["itemDesc"].lower() == name.lower():
            return champion["lootId"]
    return name


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