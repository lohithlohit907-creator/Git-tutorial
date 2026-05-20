import os
import shutil

import os
import shutil

files = os.listdir()

os.makedirs("Images", exist_ok=True)

for file in files:
    if file.endswith(".jpg"):
        shutil.move(file, os.path.join("Images", file))

print("Images moved!")