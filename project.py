import api


def main():
    connection = api.LCU_Connection()


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