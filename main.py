import sys
import tools.Quit

options = (
    {"name": tools.Quit.NAME, "desc": tools.Quit.DESC, "exec": tools.Quit.main},
)


print("""
 _______________
|    _/¯¯¯\_    |
|---------------|
|    FromeXo    |
|_______________|
""")

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
