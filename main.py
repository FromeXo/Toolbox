#!/bin/env python3
import argparse
from tools.quit.Quit import Quit
from tools.dhcp.Dhcp import Dhcp

# When done with a tool
# True: show main menu
# False: exit prog
keep_session = True

# Handle arguments
parser = argparse.ArgumentParser(prog="ToolBox", description="Collection of tools")
parser.add_argument("--tool", help="Directly load a tool", metavar="{tool}", dest="tool", required=False, default=None)
args = parser.parse_args()

# Tools
tools = (
    {"name": Dhcp.NAME, "desc": Dhcp.DESC, "exec": Dhcp.main},
    {"name": Quit.NAME, "desc": Quit.DESC, "exec": Quit.main}
)

# Directly load tools
if args.tool is not None:

    for tool in tools:
        if tool["name"].lower() == args.tool.lower():
            keep_session=tool["exec"]()

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



while keep_session is True:

    welcome_msg()

    selected_tool = prompt_for_tool(tools)

    # If the tools returns True
    # we stay in loop and let the user choose a nother tool
    # else exit the loop.
    keep_session = tools[selected_tool]["exec"]()

# Exit out of the program
Quit.main()
