#Test a user's input to see if it's a prime number!
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
clean_divide = 0  

try:
    user = int(input("Input a number to test if it's prime: ").strip())

    for i in numbers:
        if user % i == 0:
            clean_divide += 1
        else:
            pass

    if user == 0:
        print("0 isn't technically considered a number... Please try again.")
    elif user == 1:
        print("This is not a prime number")
    elif clean_divide <= 1:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")

except ValueError:
    print("Please enter numbers only!!")