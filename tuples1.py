# Write a program that takes two tuples of numbers and returns a new tuple containing the element-wise sum of the two tuples.
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (6, 7, 8, 9, 10)
list = []
for a in range(5):
    sum = tuple_1[a] + tuple_2[a]
    list.append(sum)

tuple_3 = tuple(list)
print(tuple_3) 
