import project
import api


connection = api.LCU_Connection()


def test_get_useless():
    # Assuming is an account with no useless champions
    assert project.get_useless(connection) == {}


def test_disenchant_champions():
    assert project.disenchant_champions(connection, {}) == None


def test_get_upgradeable():
    # Assuming is an account with no upgradeable champions
    assert project.get_upgradeable(connection) == {}


def test_upgrade_champions():
    assert project.upgrade_champions(connection, {}) == None