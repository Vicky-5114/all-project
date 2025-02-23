import fabbonaci
import guess_number_v1 as gv1
from guess_number_v2 import guess_number
import my_math


def guess_number():
    pass


option = input("option: ")
if option == "f":
    number = input("n=")
    print(fabbonaci.febbonaci_recursive(int(number)))
elif option == "guessv1":
    gv1.guess_number()
