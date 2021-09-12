#Password Generator
#Sidenote: originally created while following a Udemy course. Hence variable naming like 'ran4' 
#(because ran(dom)1-3 were used further up in the original file.)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

hard_range = (nr_letters + nr_numbers + nr_symbols)
hardpass = []
lettcount = 0
numcount = 0
symcount = 0
nullcount = 0

while len(hardpass) < hard_range: 
  for space in range(0, hard_range):
    sel = random.randint(0, 2)          #Random selection of letter/number/symbol for nxt character
    if sel == 0 and lettcount < nr_letters:
      lettcount += 1
      ran4 = random.randint(0, (len(letters)-1))
      hardpass.append(letters[ran4])
  
    elif sel == 1 and numcount < nr_numbers:
      numcount += 1
      ran5 = random.randint(0, (len(numbers)-1))
      hardpass.append(numbers[ran5])
    
    elif sel == 2 and symcount < nr_symbols:
      symcount += 1
      ran6 = random.randint(0, (len(symbols)-1))
      hardpass.append(symbols[ran6])
   
    elif len(hardpass) == hard_range:
      nullcount += 1
    
    else:
      nullcount += 1

      if len(hardpass) != hard_range:
        continue

print("Hard password generation:")
hard_password = "".join(hardpass)
print(hard_password)
#print(nullcount)

#Note: Nullcount was for myself, to see just how many passes this kind of program may have to do
#In order to randomly generate the requested type of password
#Unlucky ones reached up to 40 passes, which has me side-eyeing the viability.
