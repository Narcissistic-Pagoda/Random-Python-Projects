import pickle

def save_pass(serv, usern, passwd):
    pass_dict[serv] = (usern, passwd)
    print("Password saved for service:", serv)

def retrieve_pass(serv):
    if serv in pass_dict:
        return pass_dict[serv]
    else:
        return "Service not found."

try:
    with open("pass_info.pickle", "rb") as file:
        pass_dict = pickle.load(file)
except FileNotFoundError:
    pass_dict = {}

try:
    with open("master_key.pickle", "rb") as file:
        master_key = pickle.load(file)
except FileNotFoundError:
    master_key = input("Enter your 4-digit master key: ")
    with open("master_key.pickle", "wb") as file:
        pickle.dump(master_key, file)

while True:
    key = input("Enter your 4-digit master key: ")
    if key == master_key:
        print("1. Save a password")
        print("2. Retrieve a password")
        print("3. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            serv = input("Enter the name of the service: ")
            usern = input("Enter your username: ")
            passwd = input("Enter your password: ")
            save_pass(serv, usern, passwd)
        elif choice == 2:
            serv = input("Enter the name of the service: ")
            cred = retrieve_pass(serv)
            if cred != "Service not found.":
                print("Username:", cred[0])
                print("Password:", cred[1])
            else:
                print(cred)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.")
    else:
        print("Incorrect key. Try again.")

with open("pass_info.pickle", "wb") as file:
    pickle.dump(pass_dict, file)
