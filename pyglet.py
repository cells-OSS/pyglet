import pyfiglet
import sys
import subprocess
import requests
from packaging import version
import os

__version__ = "v1.0"
def get_latest_release_tag():
   try:
       url = "https://api.github.com/repos/cells-OSS/pyglet/releases/latest"
       response = requests.get(url, timeout=5)
       response.raise_for_status()
       data = response.json()
       return data["tag_name"].lstrip("v")
   except Exception as e:
       print("Failed to check for updates:", e)
       return __version__.lstrip("v")
def is_update_available(current_version):
   latest = get_latest_release_tag()
   return version.parse(latest) > version.parse(current_version.lstrip("v"))
def download_latest_script():
   latest_version = get_latest_release_tag()
   filename = f"pyglet-v{latest_version}.py"
   url = "https://raw.githubusercontent.com/cells-OSS/pyglet/main/pyglet.py"
   response = requests.get(url)
   lines = response.text.splitlines()
   with open(filename, "w", encoding="utf-8") as f:
       for line in lines:
           f.write(line.rstrip() + "\n")
   print(
       f"Current version: {__version__}, Latest: v{get_latest_release_tag()}")
   print(
       f"Downloaded update as '{filename}'. You can now safely delete the old version.")
   input("Press Enter to exit...")
   exit()
if os.path.exists("auto_update.conf"):
   with open("auto_update.conf", "rb") as auto_update_configFile:
       auto_update_config = auto_update_configFile.read().decode()
       if auto_update_config == "True":
           if is_update_available(__version__):
               print("New version available!")
               download_latest_script()

if os.path.exists("welcome_message.txt"):
   with open("welcome_message.txt", "rb") as welcome_message_file:
       welcome_message = welcome_message_file.read().decode()
       welcomeMessage = pyfiglet.figlet_format(welcome_message)
else:
   welcomeMessage = pyfiglet.figlet_format("Pyglet")

menu = """
1 = Convert text to figlet
2 = Settings

TIP: To come back to this menu at any time, type "back!"
"""
print(welcomeMessage, menu)

chooseOption = int(input("Which option would you like to choose(1/2)?: "))

if chooseOption == 1:
    while True:
        normal_ver = input("> ")

        if normal_ver.lower() == "back!":
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

        figlet_ver = pyfiglet.figlet_format(normal_ver)

        print(figlet_ver)

if chooseOption == 2:
   settingsMenu = """
===============SETTINGS===============
1 = Turn auto-update on/off
2 = Change welcome message
"""
   print(settingsMenu)
   chooseSetting = int(input("Which option would you like to choose(1)?: "))
   if chooseSetting == 1:
       aUpdateMenu = """
   ===============AUTO-UPDATE===============
   1 = Turn on
   2 = Turn off
   """
       print(aUpdateMenu)
       aUpdateOption = input(
           "Which option would you like to choose(1/2)?: ")
       if aUpdateOption.lower() == "back":
           subprocess.Popen([sys.executable] + sys.argv)
           sys.exit()
       if aUpdateOption == "1":
           with open("auto_update.conf", "wb") as auto_update_configFile:
               auto_update_configFile.write("True".encode())
               print("Changes saved successfully!")
               input("Press any key to restart...")
               subprocess.Popen([sys.executable] + sys.argv)
               sys.exit()
       if aUpdateOption == "2":
           with open("auto_update.conf", "wb") as auto_update_configFile:
               auto_update_configFile.write("False".encode())
               print("Changes saved successfully!")
               input("Press any key to restart...")
               subprocess.Popen([sys.executable] + sys.argv)
               sys.exit()

       if chooseSetting == 2:
            newWelcomeMessage = input("New welcome message: ")
            with open("welcome_message.txt", "wb") as welcome_message_file:
                welcome_message_file.write(newWelcomeMessage.encode())
                print("Changes saved successfully!")
                input("Press any key to restart...")
                subprocess.Popen([sys.executable] + sys.argv)
                sys.exit()