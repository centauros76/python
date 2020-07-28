def div(a, b):
    try:
        c = a / b
    except ZeroDivisionError as e:
        print(e)
    else:
        print(c)


div(8, 2)
div(9, 0)