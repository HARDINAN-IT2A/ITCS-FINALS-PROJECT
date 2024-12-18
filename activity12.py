odd = 0
even = 0
sum = 0

for c in range(10):
    c = eval(input(f"Enter a number {c+1} : "))
    if c:
        even += c
    else:
        odd += c
    sum += c

print(f"The sum of all number is:{sum} ")
print(f"The sum of all EVEN number is:{even} ")
print(f"The sum of all ODD number is:{odd} ")