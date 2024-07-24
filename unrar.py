import os
import subprocess
from os import listdir
from os.path import isfile, join

SOURCE_PATH = "./rar"
DESTINATION_PATH = "./unrar"
PASSWORD = "mitaku.net"

def unrar_files(password):
    onlyfiles = [f for f in listdir(SOURCE_PATH) if isfile(join(SOURCE_PATH, f))]
    print(onlyfiles)
    print("-----")
    for file in onlyfiles:
        if file.endswith(".rar"):
            print(file)
            subprocess.run(["unrar", "x", "-ad", f"{SOURCE_PATH}/{file}", DESTINATION_PATH, f"-p{password}"])
            print("done")
        else:
            print("not rar file")
    print("done")

unrar_files(PASSWORD)