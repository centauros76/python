s11 = set([1,2,3])
s12 = set("hello")

print(s11, s12)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s3 = s1 & s2
s4 = s1 | s2
print(s3, s4)

s5 = s1.intersection(s2)
s6 = s1.union(s2)
print(s5, s6)

s7 = s1 - s2
s8 = s2 - s1
print(s7, s8)

s9 = s1.difference(s2)
s10 = s2.difference(s1)
print(s9, s10)

s1.add(7)
print(s1)
s1.update([10, 11, 12])
print(s1)
s1.remove(12)
print(s1)
s1.remove(10)
print(s1)
