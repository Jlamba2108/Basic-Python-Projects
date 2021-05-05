logo='''
   ___                                    _     ___                          _             
  / _ \__ _ ___ _____      _____  _ __ __| |   / _ \___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 / /_)/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / /_\/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
/ ___/ (_| \__ \__ \\ V  V / (_) | | | (_| | / /_\\  __/ | | |  __/ | | (_| | || (_) | |   
\/    \__,_|___/___/ \_/\_/ \___/|_|  \__,_| \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                                                                                                                                                                                       
'''
print(logo)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
for i in range(1,nr_letters+1):
  password+=random.choice(letters)
for i in range(1,nr_symbols+1):
  password+=random.choice(symbols)
for i in range(1,nr_numbers+1):
  password+=random.choice(numbers)
random.shuffle(password)
mpassword=""
for i in range(0,len(password)):
  mpassword+=password[i]
print(f"Suggested password is:  {mpassword}")