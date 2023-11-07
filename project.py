import api


def main():
    connection = api.LCU_Connection()
    connection.disenchant_useless_champions()


def function_1():
    return "foo"


def function_2():
    return "bar"


def function_n():
    return "baz"


if __name__ == "__main__":
    main()