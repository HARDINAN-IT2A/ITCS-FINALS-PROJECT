money = int(input("Enter amount to deposit --> :  "))

print("DENOMINATIONS BREAKDOWN")
print("=========================")

thou = money // 1000
remaining = money % 1000

fiveh = remaining // 500
remaining = remaining % 500

twoh = remaining // 200
remaining = remaining % 200

oneh = remaining // 100
remaining = remaining % 100

fifthy = remaining // 50
remaining = remaining % 50

twen = remaining // 20
remaining = remaining % 20

ten = remaining // 10
remaining = remaining % 10

lima = remaining // 5
remaining = remaining % 5

piso = remaining // 1
remaining = remaining % 1 

print(thou, " - 1,000")
print(fiveh, " - 500")
print(twoh, " - 200")
print(oneh, " - 100")
print(fifthy, " - 50")
print(twen, " - 20")
print(ten, " - 10")
print(lima, " - 5")
print(piso, " - 1")