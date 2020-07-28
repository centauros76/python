f = open('/Users/rene.kwak/Private/source/study/python/memo.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f1 = open('/Users/rene.kwak/Private/source/study/python/memo.txt', 'r')
lines = f1.readlines()
for line in lines:
    print(line)
f1.close()

f2 = open('/Users/rene.kwak/Private/source/study/python/memo.txt', 'r')
data = f2.read()
print(data)
f2.close()
