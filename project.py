import api
import json


def main():
    connection = api.LCU_Connection()
    print(json.dumps(connection.get_useless_champions(), indent=2))


if __name__ == "__main__":
    main()