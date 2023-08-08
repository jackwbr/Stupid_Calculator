def get():
    while True:
        num1 = input("Please provide a number: ")
        num2 = input("Please provide another number: ")
        op = input("Please provide a mathamatical operator: ")
        try:
            int(num1)
            int(num2)
            break
        except ValueError:
            continue

get()