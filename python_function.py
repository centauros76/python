#def fib(n):
#    """Print a Fibonacci series up to n."""
#    a,b = 0,1
#    while a < n:
#        print(a, end=' \n')
#        a, b = b, a+b
#
#
#
#f = fib
#f(10000)


def ask_ok(prompt, retries=4, reminder='Plz try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'ye'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries - 1
        print(retries)
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok("Are you sure quit??")