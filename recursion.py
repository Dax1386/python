#itterative
def walk(steps):
    for i in range(0, steps+1):
        print(f"Walking...{i}")
walk(5)
#recursion
def walk(steps):
    if steps == 0:
        return
    print(f"Walking...{steps}")
    walk(steps - 1)
walk(5)