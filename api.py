import sys
import urllib3
import requests
import re
from base64 import b64encode
from constants import *

    
class LCU_Connection:
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        try:
            with open(LOCKFILEPATH) as lockfile:
                _, _, port, secret, protocol = lockfile.read().split(":")
        except FileNotFoundError:
            sys.exit("Lockfile was not found, are you logged in League?")

        self._url = f"{protocol}://{HOST}:{port}"

        userpass = b64encode(bytes(f"{USERNAME}:{secret}", "utf-8")).decode('ascii')
        self._headers = {"Authorization": f"Basic {userpass}"}

        try:
            self.update_loot()
            self.puuid = self.request("get", "/lol-summoner/v1/current-summoner").json()["puuid"]
            print("Connected successfully to LCU...")
        except:
            sys.exit("Failed to connect, ensure you're logged in or restart League of Legends.")


    def request(self, method: str, path: str, **kwargs) -> requests.Request:
        return requests.request(method, self._url + path, headers=self._headers, verify=False, **kwargs)
    

    @property
    def loot(self):
        return self._loot
    
    
    def update_loot(self):
        self._loot = self.request("get", "/lol-loot/v1/player-loot").json()


    @property
    def champions(self):
        champion_fragments = filter(
            lambda asset: asset["displayCategories"] == "CHAMPION",
            self.loot
        )

        return list(champion_fragments)
    

    @property
    def masteries(self):
        masteries = self.request("get", f"/lol-collections/v1/inventories/{self.puuid}/champion-mastery").json()

        return dict(map(
            lambda mastery: (mastery["championId"], mastery["championLevel"]),
            masteries
        ))


    def get_useless_champions(self) -> (dict | None):
        print("Searching for useless champions...")

        masteries = self.masteries

        useless_champions = {}

        for champion in self.champions:
            # Get champion ID
            id = int(re.findall(r"\d+", champion["lootId"])[0])

            keep = 3

            if champion["redeemableStatus"] == "ALREADY_OWNED":
                keep = 2

            try:
                if masteries[id] == 6:
                    keep = 1
                elif masteries[id] == 7:
                    keep = 0
            except:
                pass

            disenchant = (champion["count"] - keep)

            if disenchant > 1:
                print(f"Found {disenchant} {champion['itemDesc']} fragments")
            elif disenchant == 1:
                print(f"Found 1 {champion['itemDesc']} fragment")

            if disenchant >= 1:
                useless_champions[champion["lootId"]] = disenchant

        return useless_champions
    

    def disenchant_champions(self, champion_dict) -> (bool | None):
        if len(champion_dict) == 0:
            return
        
        confirmation = input("Do you want to disenchant this fragments? (yes/no)")

        if not confirmation == "yes":
            return

        for champion in self.champions:
            try:
                disenchant = champion_dict[champion["lootId"]]
            except:
                continue

            if disenchant > 1:
                print(f"Disenchanting {disenchant} {champion['itemDesc']} fragments...")
            elif disenchant == 1:
                print(f"Disenchanting 1 {champion['itemDesc']} fragment...")
            else:
                continue

            playerLootList = [champion["lootId"]] * disenchant
            self.craft(champion["disenchantRecipeName"], playerLootList)

        return True


    def get_upgradeable_champions(self) -> (dict | None):
        print("Searching for upgradeable champions...")

        upgradeable_champions = []
        essence_cost = 0

        for champion in self.champions:
            if champion["redeemableStatus"] == "ALREADY_OWNED":
                continue
            
            print(f"Found {champion['itemDesc']}")

            upgradeable_champions.append({"id": champion["lootId"], "name": champion["itemDesc"]})
            essence_cost += champion["upgradeEssenceValue"]

        return {
            "champions": upgradeable_champions,
            "essence_cost": essence_cost
        }
    
    
    def upgrade_champions(self, champion_dict) -> (bool | None):
        try:
            champions = champion_dict["champions"]
            essence_cost = champion_dict["essence_cost"]
        except:
            return

        if len(champions) == 0:
            return
        
        blue_essences = list(filter(
            lambda asset: asset["lootId"] == "CURRENCY_champion",
            self.loot
        ))[0]["count"]
        
        if (blue_essences - essence_cost) < 0:
            print("You don't have enough blue essences to upgrade all these champion fragments.")
            return
        
        confirmation = input(f"You will have {blue_essences - essence_cost} blue essences if you upgrade all, do you want to proceed? (yes/no)")

        if not confirmation == "yes":
            return

        for champion in champions:
            print(f"Upgrading {champion['name']}...")

            recipe = list(filter(
                lambda recipe: recipe["type"] == "UPGRADE",
                self.request("get", f"/lol-loot/v1/recipes/initial-item/{champion['id']}").json()
            ))[0]

            recipeName = recipe["recipeName"]
            playerLootList = []

            for slot in recipe["slots"]:
                playerLootList.append(slot["lootIds"][0])

            self.craft(recipeName, playerLootList)

        return True


    def craft(self, recipeName: str, playerLootList: list):
        self.request("post", f"/lol-loot/v1/recipes/{recipeName}/craft", json=playerLootList).json()
        self.update_loot()