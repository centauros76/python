a = "Life is too short, You need Python"
b = "a"
c = "123"

d = """This is 'Python' String"""
e = '''This is "Python" String, too'''




f = "This is \'Python\' String"
g = 'This is \"Python\" String, too'


h = '''This is 
Python
String'''


#print (h + c)

#print (c * 2)
#print (a * 2)

#print("=" * 40)
#print(a)
#print("=" * 40)


########## String length ###########
#print(len(a))

########## indexing && slicing ##########
#print(a)
#print(a[0])
#print(a[-0])
#print(a[12])
#print(a[-1])

index = 0
#for text in a:
#    print("a[{}] = {}".format(index, text))
#    index = index+1

index = -1
#for text in a:
#    print("a[{}] = {}".format(index, a[index]))
#    index = index - 1

## include first index value and not include last index value
#print(a[0:4])
#print(a[19:])
#print(a[:17])

w = "20200715Rainy"
date = w[:8]
weather = w[8:]
print("{} weather is {}".format(date, weather))
print(f"{int(date)+1} weather is {weather+'!!'}")

print(w.count("20"))
print(w.find("0"))
print(','.join(w))