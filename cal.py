def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
print(divide(10, 2))
print(multiply(10, 0))
print(subtract(10, 5))
print(add(10, 5))