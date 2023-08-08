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
            addnum5 = num1 * num2
            print("Is " + addnum5 + "what you were looking for? I don't really care.") 
            exit()
        if randNum == "3":
            print(num1 + num2)


stupid_math()