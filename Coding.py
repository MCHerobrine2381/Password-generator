import random

upper = "ABCDE"
number = "1234567890"

string = upper + number
length = 7 
password ="".join(random.sample(string, length))

import time
time.sleep(0.3)

print("\n> Password: " + password)
