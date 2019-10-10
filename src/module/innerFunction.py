a = [1, -3, 2, 0, -5, 6]

def positive(x):
    return x > 0

b = list(filter(positive, a))
print(b)



c = list(filter(lambda x: x > 0, a))
print(c)