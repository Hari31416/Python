import os
from os.path import exists

filename = "filename.txt"

print("Current directory contents:")
files = os.listdir(".")
if len(files) == 0:
    print("Directory is empty")
else:
    for file in files:
        print(file)

print("Check if file exists:")
file_exists = exists(filename)

if file_exists is True:
    print("File exists")
    print("Read the file and print the contents:")
    with open(filename, "r") as f:
        print(f.read())
else:
    print("File does not exists")

    print("Create a file, read the file and print the contents:")
    with open(filename, "w") as f:
        f.write("Hello PyScript World")
    with open(filename, "r") as f:
        print(f.read())
