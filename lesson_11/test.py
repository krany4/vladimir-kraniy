def counter(start=0):
    def inner():
        nonlocal start
        start += 1
        return start
    return inner

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2