print('직각삼각형 그리기 \n')
x = float(input('삼각형의 한 변의 길이를 입력하세요'))

for i in range(int(x)+1):
    print('* ' * i)

area = float((x ** 2) / 2)
print('넓이 : %s' % area)