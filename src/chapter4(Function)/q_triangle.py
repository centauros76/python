from pip._vendor.distlib.compat import raw_input


def triangleArea (a, b):
    area = a * b / 2
    return area

area = triangleArea(3,5)
print(area)




def exam():
    ans = raw_input('1 + 2 = ')
    return 1 + 2 == int(ans)

print(exam())
