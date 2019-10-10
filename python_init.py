#text = 'This is Python'
#text = text.capitalize()
#print(text)



#a, b = 0,1
#while a <= 30:
#    #print(a)
#    a,b = b, a+b
#
#
mammal = ['cat', 'dog', 'tiger', 'lion', 'elephant']
#for m in mammal:
#    print(m, len(m))
#
#
#for i in range(len(mammal)):
#    print(i, mammal[i])
#
#
#
#for n in range(2, 20):
#    for x in range(2, n):
#        if n % x == 0:
#            print(n, 'equals', x, '*', n//x)
#            break
#    else: #break를 통해 종료되면 실행되지 않음
#        print(n, 'is a prime number')
#

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number ", num)
        continue
    print("Found an odd number ", num)



for m in mammal:
    if m == 'cat':
        pass
    else:
        print(m)

