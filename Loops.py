tuloy_lang = True
number = 0 
while tuloy_lang:
    itanong = input("Do you wish to create a new triangle (Yes/No) ---->  ")

    if itanong.lower() == "no":
        print("program / loop terminated")
        break
    elif itanong.lower() == "yes":
        number += 1
        for x in range(1,6):
            for t in range(1, number + 1):
                for a in range(1, x+1):
                    print(a, end = " ")
                for b in range(6, x, -1):
                    print(" ", end = " ")
            print()
    continue
else:
    print("Invalid response, please input only 'yes' or 'no'")