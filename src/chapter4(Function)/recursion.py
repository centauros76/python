def hap(a, b):
    print(a+b)

def gop(a, b):
    print(a*b)

def hap_gop(a,b):
    hap(a, b)
    gop(a, b)



def countdown(n):
    if n == 0:
        print('Go!')
    else:
        print(n)
        countdown(n-1)


countdown(10)