def print_detail(parking_charge):
    if parking_charge > 150:
        parking_charge += 20
        service_charge = 20
    else:
        service_charge = 0

    print("Parking Charge:",parking_charge)
    print("Service Charge:",service_charge)
    print("Final Amount:",parking_charge+service_charge)


parking_charge = 0
parking_hours = float(input("Enter parking hours:"))
while(parking_hours<0):
    print("Enter valid hours!")
    parking_hours = float(input("Enter parking hours:"))

if parking_hours <= 2:
    parking_charge = parking_hours * 30
elif parking_hours <=5:
    parking_charge = parking_hours * 25
else:
    parking_charge = parking_hours * 20

print_detail(parking_charge)




    