# Functions with Outputs

# def my_function():
#     result = 3 * 2
#     return result

# print(my_function())
# Prints 6


# def format_name(f_name, l_name):
#     formatted_name = l_name.title() + ", " + f_name.title()
#     return formatted_name

# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# print(format_name(first_name, last_name))

# Multiple Return Values

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# def days_in_month(query_year, query_month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   leap = is_leap(query_year)
#   if leap and query_month == 2:
#     return "29"
#   else:
#     return month_days[query_month-1]
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Docstrings help define functions when we hover over them
# Must be first line after function definition and have three sets of quotes

# def kappa_function():
#     """Take your favorite thing and refer to it sarcastically, ruining all enjoyment.
#     Pee Pee Poo Poo Go away"""
#     print("poop")

# kappa_function()

# Calculator

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
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        go_again = input(f"Type \'y\' to continue calculating with {result}, type \'new\' for a new calculation,  or type \'n\' to exit: ")
        if go_again == "y":
            num1 = result
        elif go_again == "new":
            calculator()
            continuing = False
        else:
            continuing = False

calculator()