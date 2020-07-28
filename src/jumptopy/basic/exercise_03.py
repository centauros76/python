# 1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
else:
    print("none")

# 2
a = 1
result = 0
while a <= 1000:
    if a % 3 == 0:
        result += a
    a += 1
print(result)

# 3
b = 1
while b < 6:
    print("*"*b)
    b += 1

# 4
for i in range(1, 101):
    print(i)

# 5
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in scores:
    sum += score
avr = sum / len(scores)
print(avr)


# 6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

result2 = [n * 2 for n in numbers if n % 2 == 1]
print(result2)