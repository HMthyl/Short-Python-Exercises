#Temperature Conversion
#Convert to and from celsius to fahrenheit

print("Welcome. \nType 1 to convert celsius to fahrenheit \nType 2 to convert fahrenheit to celsius")
wish_ok = False
while wish_ok == False:
    wish = int(input("Enter number: "))
    if wish == 1:
        wish_ok = True
    elif wish == 2:
        wish_ok = True
    else:
        print("Enter either 1 or 2")

if wish == 1:
    c = float(input("How many degrees in Celsius? "))
    to_fahrenheit = (c/5)*9 +32
    print(f"{c}°C = {round(to_fahrenheit, 4)}°F")
elif wish == 2:
    f = float(input("How many degrees in Fahrenheit? "))
    to_celsius = (f-32)*(5/9)
    print(f"{f}°F = {round(to_celsius, 4)}°C")