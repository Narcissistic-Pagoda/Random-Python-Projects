print("Enter a number (not a string dumbass 😡) 😄:")
num = input()
try:
    num = int(num)
    if num == 0:
        print(f"You entered {num} 😝")
    elif num > 0:
        print(f"You entered a positive number, {num}! 😯")
    else:
        print(f"Shawty entered a negative number, {num} 😏🤤")
except ValueError:
    print("Didn't I tell you not to enter a string 👿")         
    
