print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def div(number: int) -> list:
    div_list = []
    for i in range(1,number+1):
        if number % i == 0:
            div_list.append(i)
    return div_list

print(div(50))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_factor(num1: int, num2:int) -> bool:
    if num2 in div(num1) or num1 in div(num2):
        return True
    else:
        return False

print(is_factor(5,50))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet


# A2a:
def alphabet_pos(letter: str):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())

print(alphabet_pos("r"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def id_generator(name_string):
    id = ""
    name_string = name_string.lower()
    for i in name_string:
        #print(i)
        id = id + str(alphabet_pos(i))
    return id

print(id_generator("Paula"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password_gen(name_string):
    id_code = id_generator(name_string)
    id_code_str = str(id_generator(name_string))
    id_sum = 0
    for letter in id_code_str:
        id_sum += int(letter)
    return int(id_code) - int(id_sum)

print(password_gen("Paula"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime(num: int) -> bool:
    count = int(2)
    while count < num-1:
        if num % count > 0:
            count+=1
        if num % count == 0:
            return False
            break
    if count == num -1:
        return True

print(is_prime("sefhksdjf"))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #



