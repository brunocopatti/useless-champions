import main
import json


with open("test_champions_large.json") as file:
    champions_large = json.loads(file.read())

with open("test_champions_short.json") as file:
    champions_short = json.loads(file.read())


def test_parse_champion_name():
    assert main.parse_champion_name(champions_large, "") == None
    assert main.parse_champion_name(champions_large, "briar") == "CHAMPION_RENTAL_233"
    assert main.parse_champion_name(champions_large, "xeRAth") == "CHAMPION_RENTAL_101"
    assert main.parse_champion_name(champions_large, "axe") == None


def test_parse_disenchant_arguments():
    assert main.parse_disenchant_arguments(champions_large, []) == {}
    assert main.parse_disenchant_arguments(champions_large, ["briar", 1, "XERATH", 1]) == {
        "CHAMPION_RENTAL_233": 1,
        "CHAMPION_RENTAL_101": 1
    }


def test_parse_upgrade_arguments():
    assert main.parse_upgrade_arguments(champions_large, []) == {}
    assert main.parse_upgrade_arguments(champions_large, ["briar", "XERATH"]) == {
        "CHAMPION_RENTAL_233": 1,
        "CHAMPION_RENTAL_101": 1
    }


def test_parse_all_champions():
    assert main.parse_all_champions([]) == {}
    assert main.parse_all_champions(champions_short) == {
        "CHAMPION_RENTAL_104": 2,
        "CHAMPION_RENTAL_234": 1,
        "CHAMPION_RENTAL_106": 1
    }