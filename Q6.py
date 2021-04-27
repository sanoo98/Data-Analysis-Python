#Question6

stre =input("Enter a Sentence: ")

countletter = 0

countdigits = 0

countunknowns = 0


for i in stre:
        if i.isalpha():
            countletter += 1
            
        elif i.isdigit():
            countdigits += 1
            
        else:
            countunknowns += 1
            
            
print("\nThe number of Letters are: ", countletter)

print("The number of Digits are: ", countdigits)

print("The number of Unknowns are: ", countunknowns)