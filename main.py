#!/bin/env python3
from tools.quit.Quit import Quit

tools = (
    {"name": Quit.NAME, "desc": Quit.DESC, "exec": Quit.main},
)


def welcome_msg():
    print("""
 _______________
|    _/¯¯¯\\_    |
|---------------|
|    Toolbox    |
|_______________|
""")


def prompt_for_tool(tools):
    selected_tool = None
    while True:

        for index, tool in enumerate(tools):
            print("{}) {}   -    {}".format(index, tool["name"], tool["desc"]))

        input_str = input("Select tool (number): ")

        if input_str.isdigit():

            selected_tool = int(input_str)

            if selected_tool > -1 and selected_tool < len(tools):
                break

        print("\nUnknown option. Please try again.\n")

    return selected_tool


keep_session = True
while keep_session is True:

    welcome_msg()

    selected_tool = prompt_for_tool(tools)

    # If the tools returns True
    # we stay in loop and let the user choose a nother tool
    # else exit the loop.
    keep_session = tools[selected_tool]["exec"]()

# Exit out of the program
Quit.main()
