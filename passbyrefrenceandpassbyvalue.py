def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]#Mutable objects like lists can be modified inside functions.
myFun(b)
print(b)

def myFun2(x):
    x = 20 #Immutable objects like integers and strings remain unchanged.

a = 10
myFun2(a)
print(a)