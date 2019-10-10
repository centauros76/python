def a(i):
    if (i > 9):
        pass
    else:
        b(i)
        a(i+1)

def b(i):
    for j in range(1,10):
        print (i, '*', j, '=', i*j)
    print('')


#a(2)
b(2)