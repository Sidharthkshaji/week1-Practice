text = input("Enter text:")
upper = lower = digit = space = character = 0
for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        character += 1

print("Uppercase:",upper)
print("Lowercase:",lower)
print("Digits:",digit)
print("Spaces:",space)  
print("Other Characters:",character)  