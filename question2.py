def calculate_amount(age,tickets):

    if age < 12:
        price = 120
        total = price * tickets
    elif age < 60:
        price = 200
        total = price * tickets
    else:
        price = 150
        total = price * tickets
    if tickets >= 5:
        discount = total * 0.1
        final_amount = total-discount
    else:
        discount = 0
        final_amount = total

    print_details(customer_name,customer_age,number_of_tickets,total,discount,final_amount)

def print_details(customer_name,customer_age,number_of_tickets,total,discount,final_amount):
    print("Name:",customer_name)
    print("Age:",customer_age)
    print("Number of tickets:",number_of_tickets)
    print("Total amount:",total)
    print("Discount:",discount)
    print("Final amount:",total-discount)
        


customer_name = input("Enter your name:")

customer_age = int(input("Enter your age:"))
while customer_age <=0:
    print("Invalid age!")
    customer_age = int(input("Enter your age:"))

number_of_tickets = int(input("Enter number of tickets:"))
while number_of_tickets <=0:
    print("Invalid number of tickets!")
    number_of_tickets = int(input("Enter number of tickets:"))

calculate_amount(customer_age,number_of_tickets)