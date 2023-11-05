print("Enter the length of the list: ")
len = input()
list = []
len  = int(len)
print("\nNow, enter the integers for the list: ")
for a in range(len):
    num = input()
    num = int(num)
    list.append(num)
print("\n")
print(f"The list of the integers is: {list}")    
print(f"And their sum is {sum(list)}")
    
    