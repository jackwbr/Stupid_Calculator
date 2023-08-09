from get import get
from whatToDo import whatToDo
from random import randint

num1, num2, op = get()
wtd = whatToDo(num1, num2, op)

def stupid_math():
    if wtd == "add":
        randNum = randint(1, 3)
        if randNum == 1:
            print("I'm on break. Come back later.")
            exit()
        if randNum == 2:
            numA = float(num1)
            numB = float(num2)
            addnum5 = numA * numB
            print("Is " + str(addnum5) + " what you were looking for? I don't really care.") 
            exit()
        if randNum == 3:
            print(num1 + num2) 
    
    if wtd == "subtract":
        randNum = randint(1, 3)
        if randNum == 1:
            print("Subtraction was never my strong suite.")
        if randNum == 2:
            numA = float(num1)
            numB = float(num2)
            num = numA + numB
            print("I've got " + num + ". That's all I can give ya,")
        if randNum == 3:
            numA = float(num1)
            numB = float(num2)
            num = numA - numB
            num = float(num)
            print(+ num + "I guess. I don't really know. ")

    if wtd == "multiply":
        randNum = randint(1, 3)
        if randNum == 1:
            print(+ num1 + "x" + num2)
        if randNum == 2:
            print("Just let me sleep!")
        if randNum == 3:
            print("Is that the one with the little 'x'?")

    if wtd == "divide":
        randNum = randint(1,3)
        if randNum == 1:
            print("Dividing is sad, why not try multiplication")
        if randNum == 2:
            print("Okay, okay, I'll be honest. I forgot how to do this")
        if randNum == 3:
            print(+ num1 + "I guess")


stupid_math()