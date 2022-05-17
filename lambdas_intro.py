def add(num1, num2):
    return num1 + num2

addition = lambda num1, num2: num1 + num2


salary = [234,567,2354,5674,644,6577,453]

bonus = list(map(lambda x: x*1.1,salary))
print(bonus)