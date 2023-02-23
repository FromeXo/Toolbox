#!/bin/env python3
from tools.Quit import Quit

tools = (
    {"name": Quit.NAME, "desc": Quit.DESC, "exec": Quit.main},
)

print("""
 _______________
|    _/¯¯¯\_    |
|---------------|
|    Toolbox    |
|_______________|
""")

selected_tool = None

while True:
    for index, tool in enumerate(tools):
        print("{}) {}    -    {}".format(index, tool["name"], tool["desc"]))

    input_str = input("Select tool (number): ")
    if input_str.isdigit():
        
        selected_tool = int(input_str)
        
        if selected_tool > -1 and selected_tool < len(tools):
            break

    print("\nUnknown option. Please try again.\n")

tools[selected_tool]["exec"]()