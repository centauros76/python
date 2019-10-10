filename = '/Users/rene.kwak/Private/source/study/python/gugudan.txt'

def gugu(list, file):
    for i in list:
        for j in range(1, 10):
            cal = '%d * %d = %d \r\n' %(i, j, i*j)
            file.write(cal)
        file.write("\n");



with open(filename, 'w') as f:
    gugu(list(range(2, 5)), f)

with open(filename, 'r') as f:
    print("="*20)
    print(f.read())
    print("="*20)

with open(filename, 'a') as f:
    gugu(list(range(5,10)), f)

with open(filename, 'r') as f:
    print("-"*20)
    print(f.read())
    print("-"*20)