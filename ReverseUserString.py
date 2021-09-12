#Reverse a user's inputted string
string = input("Give us a sentence to reverse! ")
orderstr = string.split()

orderstr.reverse()
reverse = ""
for x in orderstr:
    reverse += x
    reverse += " "
print(f"\n{reverse}")