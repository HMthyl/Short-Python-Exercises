#Find the max of the three inputted numbers
user = input("To find the max of three numbers, input three numbers, separated by a comma and space: ")
numbers = user.split(", ")

if int(numbers[0]) > int(numbers[1]) and int(numbers[0]) > int(numbers[2]):
    print(f"{numbers[0]} is the max!")
elif int(numbers[1]) > int(numbers[0]) and int(numbers[1]) > int(numbers[2]):
    print(f"{numbers[1]} is the max!")
elif int(numbers[2]) > int(numbers[0])and int(numbers[2]) > int(numbers[1]):
    print(f"{numbers[2]} is the max!")
else:
    print(f"You shouldn't see this message, something went wrong")