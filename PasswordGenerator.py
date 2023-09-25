import random

#variables, strings etc.
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Podaj długość hasła(w liczbach):"))
password = ""

for i in range(pass_len):
    password += random.choice(characters)

print(password)
