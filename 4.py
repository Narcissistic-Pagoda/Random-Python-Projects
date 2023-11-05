# Write a program that asks the user to guess a secret number between 1 and 10. 
# Keep prompting the user for guesses until they guess the correct number. 
# When the user guesses the correct number, display a message saying "Congratulations, you guessed the secret number!"   
secret  = 8
count = 0
print("""There's a secret number I've been hiding 😈

If you can guess it, you get nothing but a sense of satisfaction that you guessed it 😘

Guess the number, it's been 1 to 10 😚""")
num = input()
try:
    num = int(num)
    while num != secret:
        print("Oh you poor thing, just keep trying 🤭")
        num = int(num)
        count += 1
        continue
    print(f"Yes, you guessed the number 8 with {count} tries! 🤯")
except ValueError:
    print("Uhhh why are you entering random words weirdo 🤨🤢🤮")

