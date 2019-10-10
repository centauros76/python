num = 1
while num <= 100:
    print(num)
    num = num + 1


coffee = 10
price = 300
while True:
    money = int(input("put money : "))
    if money == price:
        print("serve coffee")
        coffee -= 1
    elif money > price:
        print("serve coffee and give change %d" % (money - price))
        coffee -= 1
    else:
        print("out of money")
        print("stock coffee : %d" % coffee)
    if coffee == 0:
        print("sold out")
        break