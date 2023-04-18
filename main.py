import calc_functions
from art import art

print(art)
print("Program written by groovinflannel")

print("*************************************")

first_number = int(input("What is your first number?\n"))


print("List of operations you can perform:\n")
for operation in calc_functions.calculator_operations:
    print(operation)

operation = input("What operation would you like to perform?\n")

second_number = int(input("What is your second number?\n"))

result = calc_functions.calculator_operations[operation](first_number, second_number)

print(f"{first_number} {operation} {second_number} = {result}")

continue_calculator = input("Continue using calculator with current result? Type y or n: \n")

while continue_calculator == 'y':
    new_first_number = result
    for operation in calc_functions.calculator_operations:
        print(operation)
    operation = input("What operation would you like to perform?\n")
    new_second_number = int(input("What is your second number?\n"))
    result = calc_functions.calculator_operations[operation](new_first_number, new_second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    continue_calculator = input("Continue using calculator with current result? Type y or n: \n")

if continue_calculator == 'n':
    print("Calculations complete. Exiting program.")

