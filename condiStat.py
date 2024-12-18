age = eval(input("Enter your age ---> : "))

if age <= 7:
    print(" - Toddler")
elif age >= 8 and age <= 13:
    print(" - Pre teen")
elif age >= 14 and age <= 18:
    print(" - Teenage")
elif age >= 19 and age <= 31:
    print(" - Early adulthood")
elif age >= 32 and age <= 45:
    print(" - Mid adulthood")
elif age >= 46 and age <= 59:
    print(" - Past adulthood")
elif age >= 60:
    print(" - Senior")

else:
    print("Invalid input")