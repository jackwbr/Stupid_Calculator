from get import get 

def whatToDo(num1, num2, op):
    if op == "+":
        wtd = "add"
    if op == "-":
        wtd = "subtract"
    if op == "*" or "x":
        wtd = "multiply"
    if op == "/":
        wtd = "divide"
    num1, num2, = num1, num2
    return wtd

if __name__ == "__main__":
    num1, num2, op = get()
    whatToDo(num1, num2, op)