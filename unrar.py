import os
import subprocess
from os import listdir
from os.path import isfile, join

def unrar_files(password):
    path = "./rar"
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)
    print("-----")
    for file in onlyfiles:
        if file.endswith(".rar"):
            print(file)
            subprocess.run(["unrar", "x", f"./rar/{file}", f"-p{password}"])
            print("done")
        else:
            print("not rar file")
    print("done")

unrar_files("mitaku.net")