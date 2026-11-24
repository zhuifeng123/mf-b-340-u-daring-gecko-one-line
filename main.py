import os

entry = "The 'rate us' popup that appears before the app even loads, because nothing says 'quality product' like holding your app hostage"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(entry)