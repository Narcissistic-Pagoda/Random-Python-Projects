list_1 = [1, 1, 3, 3, 5, 6, 7, 8, 2, 3]
list_2 = []
for a in list_1:
    if a not in list_2:
        list_2.append(a)

print(list_2)        