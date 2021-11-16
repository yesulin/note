s1={1,2}
s1.add(3)
print(s1)

s2={1,2,3,4,5}
s2.remove(2)
print(s2)

s2.discard(6)
print(s2)

s3={1,2,3,4,5}
s3.pop()
print(s3)

s3.clear()
print(s3)

s4=s2.copy()
print(s4)

s5={1,2}
s6={3,4}
print(s6.isdisjoint(s5))
