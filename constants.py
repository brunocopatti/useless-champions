import sys
import os

if sys.platform == "win32":
    LOCKFILEPATH = "C:\Riot Games\League of Legends\lockfile"
if sys.platform == "darwin":
    raise NotImplementedError("""
        macOS is not implemented, consider helping 🤓
    """)
elif sys.platform == "linux":
    raise NotImplementedError("""
        Linux is no longer available because of Vanguard 😟
    """)

HOST = "127.0.0.1"
USERNAME = "riot"