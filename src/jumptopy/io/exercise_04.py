# 1
def is_odd(num):
    if num == 0:
        print("{} is zero".format(num))
    elif num % 2:
        print("{} is odd number".format(num))
    else:
        print("{} is even number".format(num))

is_odd(3)

# 2
def calcul_avr(*args):
    sum = 0
    for i in args:
        sum += i
    avr = sum / len(args)
    return avr

print(calcul_avr(1,2,3,4,5,6))


# 3
input1 = input("Input first number : ")
input2 = input("Input second number : ")

total = int(input1) + int(input2)
print("sum is {}".format(total))


# 4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))


# 5
f1 = open('../../../ex4.txt', 'w')
f1.write('Life is too short\nyou need java')
f1.close()

f2 = open('../../../ex4.txt', 'r')
print(f2.read())
f2.close()

# 6
key_in = input("Input message : ")
with open('../../../ex_memo.txt', 'a') as ff:
    ff.write(key_in+'\n')


# 7
with open('../../../ex4.txt', 'r') as f3:
    message = f3.read()

with open('../../../ex4.txt', 'w') as f4:
    f4.write(message.replace('java', 'python'))