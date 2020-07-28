import sys

f = open('../../../new_python.txt', 'w')
for i in range(0,10):
    f.write("{} line \n".format(i))
    print("{} line".format(i))
f.close()

f2 = open('../../../memo.txt', 'a')
for i in range(0,10):
    f2.write("{} line \n".format(i))
    print("{} line".format(i))
f2.close()

with open('../../../memo.txt', 'a') as f3:
    for j in range(10, 20):
        f3.write("{} line \n".format(j))

args = sys.argv[1:]
with open('../../../new_memo.txt', 'w') as f4:
    for arg in args:
        f4.write("arg :: {} \n".format(arg))
