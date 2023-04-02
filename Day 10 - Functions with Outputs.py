# Calculator Function

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0.0:
        return "DNE"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    continuing = True
    num1 = float(input("What is the first number?: "))
    for key in operations:
        print(key)
    while continuing:
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        try:
            result = operations[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {result}")
            try:
                int(result)
                go_again = input(f"Type \'y\' to continue calculating with {result}, type \'new\' for a new calculation,  or type \'n\' to exit: ")
                if go_again == "y":
                    num1 = result
                elif go_again == "new":
                    calculator()
                    continuing = False
                else:
                    continuing = False
            except:
                go_again = input(f"You cannot continue calculating with {result}, type \'new\' for a new calculation,  or type \'n\' to exit: ")
                if go_again == "new":
                    calculator()
                    continuing = False
                else:
                    continuing = False
        except:
            go_again = input(f"Your inputs were invalid or could not be understood, type \'new\' for a new calculation,  or type \'n\' to exit: ")
            if go_again == "new":
                calculator()
                continuing = False
            else:
                continuing = False
    

calculator()