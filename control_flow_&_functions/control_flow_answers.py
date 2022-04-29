print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
counter = 1
for number in x:
    if counter <= 5:
        print(number)
        counter += 1



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for number in x:
    if number % 2 == 0:
        print(number)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
counter = 1
for number in x:
    if counter > 5:
        break
    elif number % 2 == 0:
        print(number)
    counter += 1

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
initial = []
for name in names:
    initial.append(name[0])
print(initial)



print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_index = []
for name in names:
    space_index.append(name.index(" "))
print(space_index)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials = []
for name in names:
    initials.append(name[0:1] + name[name.index(" ")+1])
print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
no_duplicates = []
for i in list_of_lists:
    if len(set(i)) == len(i):
        no_duplicates.append(i)
print(no_duplicates)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
user_prompt = True
while user_prompt:
    number = input("Please type in a number that is greater than 100... ")
    if number.isdigit():
        if int(number) >= 100:
            user_prompt = False
print(number)
# Here we need the if within an if as if the number is not a digit, them it cannot be converted to an integer



print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
user_prompt = True
while user_prompt:
    number = input("Please type in a number that is greater than 100... ")
    if number.isdigit():
        if int(number) >= 100:
            user_prompt = False
prime = True
for i in range(2, int(number)):
    if int(number) % i == 0:
        prime = False
if prime:
    print("prime")
else:
    print("not prime")
