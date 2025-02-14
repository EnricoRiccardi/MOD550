import subprocess

with open("list.txt", "r") as f:
    file = f.read()

for f in file.split('\n')[:-1]:
    print(f" Working on {f}")
    print("-----------------")
    name = f.split('/')[3]
    subprocess.run(f"git clone {f} {name}", shell=True)
    print("---- D O N E ----\n")
