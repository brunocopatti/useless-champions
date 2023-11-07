import api


def main():
    connection = api.LCU_Connection()
    connection.disenchant_useless_champions()


if __name__ == "__main__":
    main()