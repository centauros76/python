for n in range(2, 100):
    for x in range(2, n):
        print(n, x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
