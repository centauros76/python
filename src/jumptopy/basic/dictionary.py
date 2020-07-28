dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a = {1:'hi'}
b = {'a':[1,2,3]}

a[2] = 'hello'
print(a)
type(a)
a['name'] = 'rene.kwak'
print(a)
a[3] = [1,2,3]
print(a)

print(a[3])
del a[2]
print(a)

c = {1:'a', 1:'b', 1:'c'}
print(c)

print(a.keys())

for key in a.keys():
    print("a[{}] value is {}".format(key, a.get(key)))

print(a.values())

