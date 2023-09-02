import os
import re

pattern = r"manpower=(\d{4,})(\d)"

for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(filename, "r+", encoding='utf-8', errors='ignore') as file:
            contents = file.read()
            contents = re.sub(pattern, lambda m: f"manpower={m.group(1)}", contents)
            file.seek(0)
            file.truncate()
            file.write(contents)
