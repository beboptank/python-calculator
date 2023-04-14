def add(num1, num2):
    """Adds two numbers together (num1 and num2)"""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts num2 from num1"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies num1 by num2"""
    return num1 * num2


def divide(num1, num2):
    """Divides num1 by num2"""
    return num1 / num2


calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
