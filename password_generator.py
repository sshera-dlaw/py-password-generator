# Passwor Generator Using Python
import random
import string

print(string.ascii_letters)
print(string.digits)

data = int(input("Panjang Password yang diinginkan: "))
generator = string.ascii_letters + string.digits
x = []
for i in range(data):
    x.append(random.choice(generator))
print(x)
