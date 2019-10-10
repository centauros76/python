'''
import CircleModule

a = CircleModule.Math()
print(a.area(5))
'''


a = [1, -2, 3, -5, 8, -3]

def positive(num):
    if num > 0:
        return num

b = list(filter(positive, a))
print(b)

c = list(filter(lambda x: x > 0, a))
print(c)


d = int('0xea', 16)

print(d)

aa =  [1, 2, 3, 4]

bb = list(map(lambda x: x*3, aa))

print(bb)


aaa = [-8, 2, 7, 5, -3, 5, 0, 1]

max_aaa = max(aaa)
min_aaa = min(aaa)
bbb = max_aaa + min_aaa

print(bbb)


print(round(17/3, 4))