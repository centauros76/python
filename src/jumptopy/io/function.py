def add(a, b):
    return a + b


def multiAdd(*args):
    addResult = 0
    for i in args:
        addResult += i
    return addResult


def calculation(choice, *args):
    calResult = 0
    if choice == '+':
        for i in args:
            calResult += i
    elif choice == '-':
        for i in args:
            calResult -= i
    elif choice == '*':
        calResult = 1
        for i in args:
            calResult *= i
    elif choice == '/':
        calResult = 1
        for i in args:
            calResult /= i
    else:
        calResult = 0
    return calResult


## kwargs is dictionary type
def print_kwargs(**kwargs):
    keys = kwargs.keys()
    return keys


def calculration2(a, b):
    return a + b, a - b, a * b, a / b


def say_myself(name, age, man=True):
    print("My name is {}".format(name))
    print("I'm {} years old".format(age))
    if man:
        print("I'm man")
    else:
        print("I'm woman")


print(add(1, 3))
result = add(a=4, b=3)
print(result)

print(multiAdd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(calculation('*', 1, 2, 3, 4, 5))
key_list = print_kwargs(a=1, b=2)
print(list(key_list))

fa = print_kwargs
print(fa(a=1))

result = calculration2(4, 6)
add = result[0]
diff = result[1]
multi = result[2]
div = result[3]
print(add, diff, multi, div)

say_myself("rene", 45)

add_lam = lambda a, b: a + b
result = add_lam(3, 4)
print(result)