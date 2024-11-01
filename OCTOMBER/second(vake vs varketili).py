import time
import os

def vake():
    # თითოეული ნაბიჯი
    for position in range(100):
        os.system("cls")  # Windows-ზე "cls"  Linux "clear"
        print(" "* position + "  varketileli                                   ")
        print(" " * position + "  O    O    O                                         O")
        print(" " * position + " /|\\  /|\\  /|\\-->                                    /|\\")
        print(" " * position + " / \\  / \\  / \\                                       / \\")
        time.sleep(0.3)


vake()
        
