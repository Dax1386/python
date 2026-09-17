#exception handling
try:
    number=int(input("enter the number"))
    print(f"{1/number}")
except ZeroDivisionError:
    print("give valid number")
    
except ValueError:
    print("give only digit")
    
finally:  
    print("do some cleanup")