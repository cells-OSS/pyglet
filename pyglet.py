import pyfiglet

welcomeMessage = """
===============WELCOME===============
"""

print(welcomeMessage)

normal_ver = input("> ")

figlet_ver = pyfiglet.figlet_format(normal_ver)

print(figlet_ver)