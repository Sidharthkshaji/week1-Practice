values = [10, 10, 20, 20, 20, 30, 10, 10, 40]

non_consecutive = [values[0]]
j = 0
for i in values:
    if i != non_consecutive[j]:
        non_consecutive.append(i)
        j += 1
print("Original list:\n",values)
print("\nResult:\n",non_consecutive)