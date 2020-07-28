a = 6
b = 6
c = a > b
d = a == b

if d:
    print("{} is same {}".format(a, b))
elif c:
    print("{} is bigger than {}".format(a, b))
else:
    print("{} is bigger than {}".format(b, a))

s1 = [1, 2, 3, 4, 5]
s2 = ['a', 'b', 'c', 'd', 'e']
s3 = 'python'

if 'a' in s1:
    print("a in s1")
else:
    print("a in s2")

if 'p' in s3:
    print('python')
else:
    print('java')

message = 'success' if a >= 6 else 'failure'

print(message)
