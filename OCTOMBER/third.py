import time
import os

q1 = input("Hello, Do you want to be friends with Michael? : ")

def Michael():

    for position in range(100):
        os.system("cls" if os.name == "nt" else "clear")
        if position<=15:
            os.system("cls" if os.name == "nt" else "clear")
            print(" " * position + "    O")
            print(" " * position + "   /|\\ ")
            print(" " * position + "   / \\ ")
            time.sleep(0.3)
        elif position>15 and position<=35:
            if position % 2 == 0:
                print(" " * position + "   O   ")
                print(" " * position + "  \\|   ")
                print(" " * position + "   |\\ ")
        else:
                print(" " * position + "   O   ")
                print(" " * position + "  \\|/  ")
                print(" " * position + "   |   ")
                print(" " * position + "  / \\ ")
        time.sleep(0.3)
Michael()









