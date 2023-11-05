print("""Welcome to the annual Kharel Gala Party! 💃🎉

To find out whether you're eligible, please provide us your age: 😎""")

age = input()

try:
    age = int(age)  

    if age < 18:
        print("You aren't eligible for the party, also isn't it bedtime for you kid? 🤨")
    elif age >= 18:
        print("Welcome to the party brudda/sista 🥳😎")

except ValueError:
    print("You can't enter words for it dawgggg 😭😭😭")
