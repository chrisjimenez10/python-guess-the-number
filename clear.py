import os

def clear_console():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")