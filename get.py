def get():
    operators = ["+", "-", "*", "/"]
    while True:
        num1 = input("Please provide a number: ")
        num2 = input("Please provide another number: ")
        op = input("Please provide a mathamatical operator: ")

        try:
            int(num1)
            int(num2)
        except ValueError:
            print("PLEASE ENTER VALID NUMBERS")
            continue      
        if op in operators:
            break
        else: 
            print("Invalid operator, please submit a valid one")
            continue

if __name__ == "__main__":
    get()