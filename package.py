import hashlib
import json
import os
import shutil

hashes = {}

for folder in os.listdir("decks"):
    format = os.path.join("decks", folder)
    zip = shutil.make_archive(f"{folder}", "zip", format)
    with open(zip, "rb") as f:
        hashes[os.path.basename(zip)] = {"sha1": hashlib.sha1(f.read()).hexdigest()}

with open("hashes.json", "w") as f:
    json.dump(hashes, f, indent=2)
