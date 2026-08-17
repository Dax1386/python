def interest(p,t,r):
    return (p*t*r)/100

p = float(input("Enter principal amount: "))
t = float(input("Enter time period: "))
r = float(input("Enter rate of interest: "))

result = interest(p,t,r)
print("Simple Interest is:", result)