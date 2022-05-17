num1 = 3
num2 = 34

def add():
    result = num1 + num2
    def divide():
        half = result/2
        return half
    return divide()


print(num1)
print(num2)


print(add())