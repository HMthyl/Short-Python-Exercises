#1. Print out numbers between 1500-2700 divisible by 7 & 5
for x in range(1500,2701):
    if x % 7 == 0 and x % 5 == 0:
        print(x)

#2. Print the numbers 0-6 without Python printing '3' or '6'
for x in range(6+1):
    if x == 3 or x == 6:
        continue
    else:
        print(x)