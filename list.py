number_list = [12, 34, 56, 7, 56, 14, 6, 32, 45, 24]
operation = sum(number_list)
print(operation)

# prints the reverse
number_list =[12, 34, 56, 7, 56, 14, 6, 32, 45, 24]
i = len(number_list) - 1 #starts from the last index
while i >= 0:
    print(number_list[i])
    i -= 1