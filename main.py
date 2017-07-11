import time
import os

if not os.path.exists("sinema"):
    os.system("mkdir sinema")

def repeat(number):
    for i in range(number):
        print("hello")


def program(dosya):
    time.sleep(5)
    os.system("touch output.txt")
    os.system("rm " + dosya)
    print("your file is prepared")


# Pseudo-Downloaded file
os.system("touch dosya.txt")
program("dosya.txt")
os.system("mv output.txt sinema/23.txt")