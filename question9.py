message = input("Enter the message : ")
first_five = message.strip()[:5]
last_five = message.strip()[-5:]
middle = message.strip()[2:7]
every_2nd = message.strip()[::2]
reverse = message.strip()[::-1]
without_end = message.strip()[1:-1]

print("First 5 Characters:",first_five)
print("Last 5 Characters:",last_five)
print("Characters from Index 2 to 7:",middle)
print("Every Second Character:",every_2nd)
print("Message in Reverse:",reverse)
print("Message without first and last character:",without_end)