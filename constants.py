import sys
import os

if sys.platform == "linux":
    # This assumes the user have Wine with Lutris
    LOCKFILEPATH = f"/home/{os.getlogin()}/Games/league-of-legends/drive_c/Riot Games/League of Legends/lockfile"
elif sys.platform == "win32":
    LOCKFILEPATH = "C:\Riot Games\League of Legends\lockfile"
    # TODO: macos path

HOST = "127.0.0.1"
USERNAME = "riot"