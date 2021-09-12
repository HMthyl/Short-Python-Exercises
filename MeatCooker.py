#Create a program that provides recommended cooking times for types/weights of meat

print("What are you cooking today? \n1. Beef (well done) \n2. Chicken \n3. Lamb \n4. Pork")
cut = input("Please type the meat's numer and its weight in kg, separated by a space, \n e.g, cooking 0.6kgs of lamb = 3 0.6). \nWhat's cookin': ")
prepcut = cut.split()
numkg= float(prepcut[1])

if int(prepcut[0]) == 1:
    time = str((numkg*50)+20)
    meat = "beef"
    weight = str(numkg)
elif int(prepcut[0]) == 2:
    time = str((numkg*45)+20)
    meat = "Chicken"
    weight = str(numkg)
elif int(prepcut[0]) == 3:
    time = str((numkg*60)+30)
    meat = "Lamb"
    weight = str(numkg)
elif int(prepcut[0]) == 4:
    time = str((numkg*70)+35)
    meat = "Pork"
    weight = str(numkg)
else:
    print("Something went wrong! Please check your formatting!")
    
print(f"The cooking time for a piece of {meat} that weighs {weight}kg(s) is {time} minutes")