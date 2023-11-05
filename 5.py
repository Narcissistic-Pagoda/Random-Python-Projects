
print("Enter a positive integer: ")
num = input()
try:
    num = int(num)
    print("\n \n")
    if num <= 0:
        print("I told you to enter a positive integer dumbass 😭")
    elif num > 0:
        if num%2 == 0:
            for i in range(2, num+1, 2):
                print(f"{i}")
        elif num%2 != 0:
            for i in range(1, num+1, 2):
                print(f"{i}")
except ValueError:
    print("No strings hunny 😚")
