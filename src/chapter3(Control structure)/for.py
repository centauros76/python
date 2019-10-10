'''
family = ['mother', 'father', 'daughter', 'daughter']

for name in family:
    print('%s %s' % (name, len(name)))

'''


'''
a = range(2, 9)
for i in a:
    print('i =', i)


for j in range(2, 10):
    print('j =', j)
'''


marks = [90,28, 45, 75, 80, 75, 55]
number = 0
'''
for point in marks:
    number += 1
    if point < 60:
        print("%d 학생은 불합격입니다." % number)
    else:
        print("%d 학생은 합격입니다." % number)


for point in marks:
    number += 1
    if point < 60: continue
    else :
        print("%d번 학생은 합격입니다." % number)


for number in range(len(marks)):
    if marks[number] < 60 : continue
    print("%d번 학생은 합격입니다." % (number+1))

#gugudan
for i in range(2, 10):
    for j in range(1, 10):
        print(i, " * ", j, " = ", i*j)
    print("")
'''
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for point in a:
    sum += point
avr = sum / len(a)
print(avr)



