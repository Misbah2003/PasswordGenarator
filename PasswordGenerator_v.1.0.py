import random # SO THAT A RANDOM PASSWORD CAN BE GENERATED
import colorama # TO HIGHLIGHT SOME TEXT
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def PasswordGenerator():
    converted = False
    while converted != True:
        length_str = input(Fore.YELLOW + "How long" + Fore.WHITE + " should be your passwort? / How many chars shuld it have?: ")
        try:
            length = int(length_str)
            converted = True

        except Exception:
            # IF THE USER DOSEN'T ENTER ANYTHING, THE DEFAULT-LENGTH WILL BE 9-CHARS LONG
            if length_str == "" or length_str:
                length = 9 # DEFAULT
                converted = True

            else:
                print(Fore.YELLOW + "Sorry, but your input is invalid" + Fore.WHITE + ", please enter a number or nothing\nIf you don't enter anything, the default length will be 9")


    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "§$%&?*+~#@;._"

    all = lower + upper + numbers + symbols
    password = "".join(random.sample(all, length))

    print("Your password: " + Fore.YELLOW + password)

    run_again = input("Do you want to have a other or " + Fore.YELLOW + "new password?" + Fore.WHITE + "\nEnter " + Fore.YELLOW + "[Y]" + Fore.WHITE + " for yes or " + Fore.YELLOW + "[n]" + Fore.WHITE + " for no: ")
    if run_again.lower() == "y":
        PasswordGenerator()

    else:
        exit()

print(PasswordGenerator())
