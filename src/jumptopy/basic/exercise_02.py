# 1
hong = (80, 75, 55)
sum = 0
for i in hong:
    sum = sum + i
avr = sum / len(hong)
print("hong's score kor : {}, eng : {}, math : {}, total : {}, avr : {}".format(hong[0], hong[1], hong[2], sum, avr))

# 2
a = 13 % 2
if a == 1:
    print("{} is odd number".format(13))
else:
    print("{} is even number".format(13))

# 3
pin = "881120-1068234"
print(pin[0:pin.index('-')])
print(pin[pin.index('-') + 1:])

# 4
pin = "881120-1068234"
gen = int(pin[7])
gen = gen % 2
if gen == 0:
    print("Male")
else:
    print("Female")

# 5
a = "a:b:c:d"
print(a.replace(":", "#"))

# 6
nums = [1, 3, 5, 4, 2]
nums.sort()
print(nums)

# 7
strs = ['Life', 'is', 'too', 'short']
print(" ".join(strs))

# 8
t = (1, 2, 3)
t = t + (4,)
print(t)

# 9
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
a[250] = 'python'
print(a.items())
print(a[('a',)])

# 10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

# 11
aa = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(aa)
print(b)

# 12
a = b = [1, 2, 3]
a[1] = 4
print(b)