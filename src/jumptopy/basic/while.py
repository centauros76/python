coffee = 30
money = 5000
cost = 350
sell_count = 0
while money > cost and coffee > 0:
    coffee = coffee - 1
    money = money - cost
    sell_count = sell_count + 1
    print("==="*10)
    print("get coffee")
    print("stock coffee {}".format(coffee))
    print("stock money {}".format(money))
    print("sell coffee count {}".format(sell_count))
    print("==="*10)

a = 0
while a < 100:
    a = a + 1
    if a % 2 == 0: continue
    print("{} is odd number".format(a))
