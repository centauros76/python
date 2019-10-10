filename = '/Users/rene.kwak/Private/source/study/python/gugudan.txt'



result = open(filename, 'w')
for i in range(2, 6):
    for j in range(1, 10):
        cal = '%d * %d = %d \r\n' %(i, j, i*j)
        result.write(cal)
    result.write('\r\n')
result.close()


file = open(filename, 'r')
print('='*20)
print(file.read())
print('='*20)
file.close()

result = open(filename, 'a')
for i in range(6, 10):
    for j in range(1, 10):
        cal = '%d * %d = %d \r\n' %(i, j, i*j)
        result.write(cal)
    result.write('\r\n')
result.close()

file = open(filename, 'r')
print('='*20)
print(file.read())
print('='*20)
file.close()


