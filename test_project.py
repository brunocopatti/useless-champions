import project
import api


connection = api.LCU_Connection()


def test_get_useless():
    # Assuming is an account with no useless champions
    assert project.get_useless(connection) == {}


def test_disenchant_champions():
    assert project.disenchant_champions(connection, {}) == None


def test_get_upgradeable():
    ...


def test_upgrade_champions():
    ...

