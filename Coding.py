import random

upper = "ABCDE"
number = "1234567890"

string = upper + number
length = 7 
password ="".join(random.sample(string, length))

print("> Password: " + password)
