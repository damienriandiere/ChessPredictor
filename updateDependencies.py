"""Module for modifying and installing dependencies in requirements.txt.

This module detects the operating system and modifies the requirements.txt file
based on the system. It then installs the dependencies and updates the requirements.txt
file with the exact versions of the installed packages.
"""

import os
import platform
import subprocess

def modifyRequirements():
    """
    Modifies the requirements.txt file based on the operating system.

    If the system is Windows, it replaces '==' with '>='. If the system is Linux,
    it uses 'sed' to replace '==' with '>='.

    Returns:
        bool: True if the modification is successful, False otherwise.
    """
    system = platform.system()
    requirements_file = "requirements.txt"

    if not os.path.exists(requirements_file):
        print(f"The file {requirements_file} is not found.")
        return False

    try:
        if system == "Windows":
            print("Modifying requirements.txt for Windows...")
            subprocess.run(
                ["powershell", "-Command",
                "(Get-Content requirements.txt) -replace '==', '>=' | Set-Content requirements.txt"],
                check=True
            )
        elif system == "Linux":
            print("Modifying requirements.txt for Linux...")
            subprocess.run(["sed", "-i", "s/==/>=/g", requirements_file], check=True)
        else:
            print(f"Unsupported system: {system}")
            return False

        print("requirements.txt file modified successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error modifying {requirements_file}: {e}")
        return False

def installAndFreeze():
    """
    Installs the dependencies from requirements.txt and updates this file
    with the exact versions of the installed packages.

    Returns:
        None
    """
    try:
        print("Installing dependencies...")
        subprocess.run(["pip", "install", "-r", "requirements.txt", "--upgrade"], check=True)

        print("Updating requirements.txt with installed versions...")
        with open("requirements.txt", "w", encoding="utf-8") as f:
            subprocess.run(["pip", "freeze"], stdout=f, check=True)

        print("Dependencies installed and requirements.txt updated.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation or update: {e}")

if __name__ == "__main__":
    if modifyRequirements():
        installAndFreeze()
