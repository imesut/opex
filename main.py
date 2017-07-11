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


def process(dosya, output):
    os.system("touch " + dosya)
    program(dosya)
    os.system("mv output.txt sinema/" + output)

process("dosya.txt", "23.txt")