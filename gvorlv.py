s = "Python is great!"

def fun():
    global s
    s += "for data science"   # Modify global variable
    print(s)
    s = "i am a Python developer"  # Reassign global
    print(s)

fun()
print(s)