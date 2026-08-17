def compund_interest(p,r,t):
    return p * (1 + r/100)**t - p
p=float(input("Enter principal amount: "))
t=float(input("Enter time period: "))
r=float(input("Enter rate of interest: "))

CI=compund_interest(p,r,t)
print("Compound Interest is:", CI)