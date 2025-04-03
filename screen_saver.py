import random
import os
from math import floor
from time import sleep

TIME_SECONDS = 0.2

def main():
    os.system("color 02")
    os.system("cls")
    
    height = os.get_terminal_size().lines
    for i in range(height):
        print("")

    while True:
        size = floor(os.get_terminal_size().columns / 4)
        number = random.randint(0, 9999999)
        spaces_raw = random.randint(1, size)
        spaces_adjusted = ((spaces_raw * 4) - len(str(number)))

        print(f"{" " * spaces_adjusted}{number}")
        sleep(TIME_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("color 07")
        os.system("cls")
