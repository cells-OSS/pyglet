import pyfiglet
import sys
import subprocess

welcomeMessage = """
===============WELCOME===============
"""

menu = """
1 = Convert text to figlet

TIP: To come back to this menu at any time, type "back!"
"""
print (welcomeMessage, menu)

chooseOption = input("Which option would you like to choose(1)?: ")

if chooseOption == "1":
    while True:
        normal_ver = input("> ")

        if normal_ver.lower() == "back!":
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit() 

        figlet_ver = pyfiglet.figlet_format(normal_ver)

        print(figlet_ver)