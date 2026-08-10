seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
booked = False
for i, n in enumerate(seats):
    print(f"Seat {i+1}: {n}")

seat_number = int(input("Enter the seat number:"))
while booked == False:
    
    while seat_number > len(seats) or seat_number <= 0:
        print("Enter valid seat number.")
        seat_number = int(input("Enter the seat number:"))
    if seats[seat_number-1] == "Available":
        print("Seat booked successfully.")
        seats[seat_number-1] = "Booked"
        booked = True
    else:
        print("Seat already booked!")
        seat_number=0

    print("Total seats:",len(seats))
    print("Available seats:",seats.count("Available"))
    print("Booked seats:",seats.count("Booked"))