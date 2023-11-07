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
    

    def disenchant_useless_champions(self):
        print("Searching for useless champions...")

        masteries = self.request("get", f"/lol-collections/v1/inventories/{self.puuid}/champion-mastery").json()
        masteries = dict(map(
            lambda mastery: (mastery["championId"], mastery["championLevel"]),
            masteries
        ))

        disenchant_list = []

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

            if disenchant > 0:
                print(f"{disenchant} {champion['itemDesc']} fragments")

            disenchant_list.extend(
                [champion["lootId"]] * disenchant
            )

        if len(disenchant_list) == 0:
            sys.exit("You don't have useless champion fragments")


    def craft(self, recipeName: str, playerLootList: list):
        response = self.request("post", f"/lol-loot/v1/recipes/{recipeName}/craft", json=playerLootList).json()
        self.update_loot()
        return response