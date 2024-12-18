def grocery_purchase():
#Questions
    purchase = input("Did you buy a grocery? Yes/No:   ").stip().lower()
    if purchase != "Yes":
        print("Thank you for trusting")
    return
item = input("Name of the item:   ")
price = float(input("Price of the item:   "))
age = eval(input("Age: "))
amount = float(input("Amount given:  "))
#Discount
discount = 0
if age >= 60:
    discount = price * 0.052 #5.2 discount
#Tax
Tax = price * 0.123
#Calculate total price
Totalamount = price + Tax
#If had discount
discounted = price + Tax - discount
#Calculate the change
change = amount - discounted

#THE OUTPUT
print(f"Hi customer, you purchased a {item} , with a price of {price:.2f} plus 12.3% tax ({Tax:.2f}) with the total amount of ")
print(f"Total of {Totalamount}.")
print(f"Amount given: {amount}")
print(f"Discounted price: {discounted}")
print(f"Change: {change}")
