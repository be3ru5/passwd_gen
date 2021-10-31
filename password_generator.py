#!/usr/bin/python3

import random, string

lower = random.sample(string.ascii_lowercase,5)
upper = random.sample(string.ascii_uppercase,5)
num = random.sample(string.digits,3)
symbols = random.sample(['!','@','#','$','&'],3)

print ("".join(random.sample(lower + upper + num + symbols,16)))
