import operator

a = [(3, 25), (15, 6), (11, 9), (23, 3), (13, 15)]
result = []
result_dic = dict()
index = 0
for (one, two) in a:
    index = index + 1
    temp = one + two
    result.append(temp)
    print("{}".format(temp))
    result_dic[index] = temp

result.sort()
print(result)

print(sorted(result_dic.items(), key=operator.itemgetter(1), reverse=True))

scores = [90, 78, 69, 38, 98, 76, 88]
num = 0
for score in scores:
    num = num + 1
    #    if score >= 80:
    #        print("{}번 수험생 {}점으로 합격입니다.".format(num, score))
    if score < 80:
        continue
    print("{}번 수험생 {}점으로 합격입니다.".format(num, score))

xr = range(2, 10)
yr = range(1, 10)
for x in xr:
    for y in yr:
        print("{} * {} = {}".format(x, y, x * y))
    print(" ")

nums = [1, 2, 3, 4]
result = []
for num in nums:
    result.append(num * 3)
print(result)

result2 = [num * 3 for num in nums]
print(result2)

result3 = [num * 2 for num in range(1, 101) if num % 2 == 0]
print(result3)

result4 = [x * y for x in range(2, 10)
           for y in range(1, 10)]
print(result4)
