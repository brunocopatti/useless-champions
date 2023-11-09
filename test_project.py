import project
import json


with open("test_champions_large.json") as file:
    champions_large = json.loads(file.read())

with open("test_champions_short.json") as file:
    champions_short = json.loads(file.read())


def test_parse_champion_name():
    assert project.parse_champion_name(champions_large, "") == None
    assert project.parse_champion_name(champions_large, "briar") == "CHAMPION_RENTAL_233"
    assert project.parse_champion_name(champions_large, "xeRAth") == "CHAMPION_RENTAL_101"
    assert project.parse_champion_name(champions_large, "axe") == None


def test_parse_champion_arguments():
    assert project.parse_champion_arguments(champions_large, []) == {}
    assert project.parse_champion_arguments(champions_large, ["briar", 1, "XERATH", 1]) == {
        "CHAMPION_RENTAL_233": 1,
        "CHAMPION_RENTAL_101": 1
    }


def test_parse_champions():
    assert project.parse_champions([]) == {}
    assert project.parse_champions(champions_short) == {
        "CHAMPION_RENTAL_104": 2,
        "CHAMPION_RENTAL_234": 1,
        "CHAMPION_RENTAL_106": 1
    }