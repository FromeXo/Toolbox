#!/bin/env python3
from tools.Quit import Quit

options = (
    {"name": Quit.NAME, "desc": Quit.DESC, "exec": Quit.main},
)


print("""
 _______________
|    _/¯¯¯\_    |
|---------------|
|    Toolbox    |
|_______________|
""")
userSel = None
while True:
    for index, tool in enumerate(options):
        print("{}) {}    -    {}".format(index, tool["name"], tool["desc"]))

    inputStr = input("Select tool (number): ")
    if len(inputStr) > 0:
        userSel = int(inputStr)
        if userSel > -1 and userSel < len(options):
            break
    print("\nPlease select a number in the list.")

options[userSel]["exec"]()