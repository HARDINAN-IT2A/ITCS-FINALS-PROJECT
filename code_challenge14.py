total_sum = 0 

#continue to ask user for a number
while True:
    try:
        #Ask the user to enter a number
        user = int(input("Enter a number ---->   "))
        #Add the number for total sum
        total_sum += user

    except ValueError:
        #If the users enters an invalid number like string, stop the loop
        print("Please enter a valid number")
        break
#Output
print("Loop has terminated")
print("The sum of all the numbers given is:", total_sum)