import api
import sys
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

    if args.disenchant != None:
        print("disenchant champions", args.disenchant)

    if args.upgrade != None:
        print("upgrade champions", args.upgrade)

if __name__ == "__main__":
    main()