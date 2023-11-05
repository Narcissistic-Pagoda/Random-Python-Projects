# Write a program that checks if a given set is a subset of another set and returns True or False.
set_1 = {1, 2, 4, 3, 5, 6, 7, 7}
set_2 = {1}
list_1 = sorted(list(set_1))
list_2 = sorted(list(set_2))
print(set_2.issubset(set_1))