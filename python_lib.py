from random import random
import math
import requests
from classes_intro.more_oop import A

rand_float = random()

print(math.floor(rand_float))

request_data = requests.get("https://www.bbc.co.uk/")

obj_a = A()

