from get import get 

def whatToDo(num1, num2, op):
    if op == "+":
        wtd = "add"
    if op == "-":
        wtd = "subtract"
    if op == "*":
        wtd = "multiply"
    if op == "/":
        wtd = "divide"
    num1, num2, = num1, num2
    return wtd

num1, num2, op = get()
whatToDo(num1, num2, op)