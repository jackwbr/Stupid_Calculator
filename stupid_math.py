from get import get
from whatToDo import whatToDo
from random import randint

num1, num2, op = get()
wtd = whatToDo(num1, num2, op)

def stupid_math():
    if wtd == "add":
        randNum = randint(1, 3)
        if randNum == "1":
            print("I'm on break. Come back later.")
            exit()
        if randNum == "2":
            addnum = num1 * num2
            print(+addnum "This is ") 
            exit()
        if randNum == "3":
            print("")


stupid_math()