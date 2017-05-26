def squared(num):
    try:
        if int(num):
            return num * num
    except ValueError:
        return num * len(num)



print(squared("dog"))
print(squared(2))
print(squared(5))
