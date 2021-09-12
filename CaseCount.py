#Write a Python function that accepts a string
#And then calculates the number of Upper and Lower case letters in that string.

def casecount(letsgo):
    upper = 0
    lower = 0
    special = 0
    longstring= letsgo.replace(" ","")
    for letter in longstring:
        if letter.islower() == True:
            lower += 1
        elif letter.isupper() == True:
            upper += 1
        else:
            special += 1
    print(f"Your sentence contains {upper} upper case letters, {lower} lower case letters and {special} special characters")

test = "Here's a SENTENCE to TEST what's going on in the function"
casecount(test)