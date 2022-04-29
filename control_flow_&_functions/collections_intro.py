def greeting(name: str = "Paula") -> str:
    return "Hello " + name

#print(greeting())

def division_of_numbers(num1=10, num2=5):
    return num1/num2

print(f"The greeting is: {greeting()}, Division here: {division_of_numbers()}")

def add(num1):
    num2 = division_of_numbers()
    return num2 + num1

print(add(5))