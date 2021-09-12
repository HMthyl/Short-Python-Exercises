#Find numbers between 100 and 400 (both included) where each digit of a number is an even number 
#(zero is not an even number)
#Print the resulting outcome in a comma-separated sequence
comma_separated = []

for x in range(100,401):
    wx = str(x)
    i = int(wx[0])
    ii = int(wx[1])
    iii = int(wx[2])
    if "0" in wx:
        continue
    elif i % 2 == 0:
        if ii % 2 == 0 and iii % 2 == 0:
            comma_separated.append(wx)
        else:
            continue

sequence = ", ".join(comma_separated)
print(sequence)