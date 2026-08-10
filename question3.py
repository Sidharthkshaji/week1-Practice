number = int(input("Enter number:"))
even_count = 0
odd_count = 0
for i in range(1,11):
    if number*i % 2 == 0:
        print(f"{number} x {i} = {number*i} - Even")
        even_count += 1
    else:
        print(f"{number} x {i} = {number*i} - Odd")
        odd_count += 1

print("Even Results:",even_count)
print("Odd Results:",odd_count)
    