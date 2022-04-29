print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def divisors(number: int) -> list:
    divisors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:


def is_factor(num1: int, num2: int) -> bool:
    if num2 in divisors(num1) or num1 in divisors(num2):
        return True
    else:
        return False


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:


def alphabet_position(letter: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:


def id_generator(name_string: str) -> str:
    id = ""
    for letter in name_string:
        id = id + str(alphabet_position(letter))
    return id


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


def password_generator(name_string: str) -> str:
    number = 0
    for i in id_generator(name_string):
        number += int(i)
    return str(int(id_generator(name_string)) - number)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def is_prime(number) -> bool:
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False
    return prime


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


def is_prime2(number) -> bool:
    if number.isdigit():
        prime = True
        for i in range(2,int(number)):
            if int(number) % i == 0:
                prime = False
        return prime
    else:
        print("please enter a digit")

print(is_prime2("10"))
# -------------------------------------------------------------------------------------- #