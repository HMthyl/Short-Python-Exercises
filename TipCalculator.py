#Tip Calculator

print("Welcome to the tip calculator.")
total_bill = float(input("What was your total bill?\n€"))
percentage = float(input("Thanks! What percentage tip do you want to give? 10, 12 or 15? \nPlease enter number only, no % sign: \n"))
diners = int(input("And finally, how many people to split the bill?\n"))

percentage_value = (total_bill / 100) * percentage
costpp = (total_bill + percentage_value) / diners

print(f"Each person should pay: €{costpp:.2f}")