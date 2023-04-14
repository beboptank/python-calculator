import calc_functions
from art import art

print(art)
print("Program written by groovinflannel")

print("*************************************")

first_number = int(input("What is your first number?\n"))
second_number = int(input("What is your second number?\n"))

print("List of operations you can perform:\n")
for i in range(1, 5):
    if i == 1:
        print("+")
    elif i == 2:
        print("-")
    elif i == 3:
        print("*")
    else:
        print("/\n")

operation = input("What operation would you like to perform?\n")

result = calc_functions.calculator_operations[operation](first_number, second_number)

print(result)

