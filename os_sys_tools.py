     ##-----1-amliy

import os
import subprocess
import sys


if len(sys.argv) < 2:
    print("Foydalanish: python os_sys_tools.py fayl_nomi [papka]")
    sys.exit(1)

file_name = sys.argv[1]
tmp_folder = sys.argv[2] if len(sys.argv) > 2 else "."

print("1. Joriy papka:")
for name in os.listdir():
    print(name)

print(f"\n2. {file_name} fayli mazmuni:")
with open(file_name, encoding="utf-8") as file:
    print(file.read())

print("3. Tizim buyrug'i:")
command = "dir" if os.name == "nt" else "ls -la"
subprocess.run(command, shell=True, check=True)

print("4. PATH:")
print(os.environ.get("PATH", ""))

print(f"5. {tmp_folder} papkasidagi .tmp fayllar:")
for name in os.listdir(tmp_folder):
    if name.lower().endswith(".tmp") and os.path.isfile(os.path.join(tmp_folder, name)):
        print(name)