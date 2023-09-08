from get import get
from whatToDo import whatToDo
from random import randint

num1, num2, op = get()
wtd = whatToDo(num1, num2, op)

def stupid_math():
    if wtd == "add":
        randNumAdd = randint(1, 3)
        if randNumAdd == 1:
            print("I'm on break. Come back later.")
            exit()            
        if randNumAdd == 2:
            numA = float(num1)
            numB = float(num2)
            addnumlol = numA * numB
            print("Is " + str(addnumlol) + " what you were looking for? I don't really care.") 
            exit()
        if randNumAdd == 3:
            print(num1 + num2) 
    
    if wtd == "subtract":
        randNum = randint(1, 3)
        if randNum == 1:
            print("Subtraction was never my strong suite.")
        if randNum == 2:
            numA = float(num1)
            numB = float(num2)
            num = numA + numB
            print("I've got " + str(num) + ". That's all I can give ya.")
        if randNum == 3:
            numA = float(num1)
            numB = float(num2)
            num = numA - numB
            print( str(num) + " I guess. I don't really know. ")

    if wtd == "multiply":
        randNum = randint(1, 3)
        if randNum == 1:
            print(num1 + "x" + num2)
        if randNum == 2:
            print("Just let me sleep!")
        if randNum == 3:
            print("Is that the one with the little 'x'?")

    if wtd == "divide":
        randNum = randint(1,4)
        if randNum == 1:
            print("Dividing is sad, why not try multiplication?")
        if randNum == 2:
            print("Okay, okay, I'll be honest. I forgot how to do this.")
        if randNum == 3:
            str(num1)
            print(num1 + " I guess")
        if randNum == 4:
            rando = randint(1,99999)
            print( str(rando) + ". What, did you expect the right answer?")

stupid_math()