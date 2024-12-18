password = input("Enter your password ---> : ")

if password.lower() == "iloveyou123":
    print("Access Granted")
    print("We hope you to enjoy using this system!")
elif password.lower() == "labyutoo":
    print("Successfully entered!")
    print("You may now enjoy our system!")
else:
    print("Oh no! Access denied")
print("System exit, thank you for using this system")