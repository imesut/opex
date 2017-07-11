import time
import os

if not os.path.exists("sinema"):
    os.system("mkdir sinema")

def repeat(number):
    for i in range(number):
        print("hello")


def program():
    time.sleep(5)
    print("your file is prepared")


# Pseudo-Downloaded file
os.system("touch dosya.txt")
program()
os.system("mv dosya.txt sinema/23.txt")