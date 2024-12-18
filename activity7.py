#introduction to conditional statement

gold = 0 
miner = input("Hi good day! What is your name?  ---> ")

isGold = input("is the mineral gold? ---> ")

if isGold.lower()== "yes" :
    gold += 1
    print(f"Hi good day! {miner} , Your total number of gold is {gold}")
else:
    print(f"Hi good day! {miner} , Your total number of gold is {gold}")
    