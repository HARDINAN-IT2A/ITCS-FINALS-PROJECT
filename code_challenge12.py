for  x in range(8,1,-1):
    for z in range(x,0, -1):
        print(" ", end = " ")

    for y in range(7, x, -1):
        print("*", end = " ")

    for a in range(7, x, -1):
        print("*", end= " ")
    print()

for  x in range(5,0,-1):
    for z in range(6,0,-1):
        print(" ", end = " ")
    
    for y in range(1,2):
        print("*", end = " ")

    for a in range(1,2):
        print("*", end= " ")
    print()