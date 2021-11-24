import pyperclip, shelve, sys

with open("mcb") as f:
    pyperclip.copy(f.write())
