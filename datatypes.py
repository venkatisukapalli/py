#datatypes
#diff between list and tuple
# list is unsafe tuple is safe
# list is created with [] and constructor list()
# list maintain insertion order and allows duplicates
#task 1 creating a list and passing some elements to it and printing their length
a=[1,2,3,4,5,6,7,8,9,10]
print(type(a))
print(len(a))

#printing order
b=[4.2,4.2,1.1,-2]
print(b)
print(type(b))
print(len(b))
print(b[1])

c=['venkata'+'naga'+'bhaskar'+'Isukapalli']
print(c)
print(len(c))

l1=[10,20,30,40,50,50,60,70,80,90,90]
#   1  2  3  4  5  6  7  8  9  10  11    length
#   0  1  2  3  4  5  6  7  8   9  10    positions
print(l1)
print(len(l1))
print(l1[1])
print(l1[-4])
#if we have duplicate value will they share same memory or no ?
l2=[10,20,20,30,40,40,50,50,60,70,80,90,90]
print(id(l2[2]), id(l2[3]))

#slicing
l5=[10,20,30,40,40,50,60,70,80,90,90]
#   [0 1  2  3  4  5  6  7  8  9  10 ]
print(l5[1: 9: 1])

print(l5[1: 9: 2])
print(l5[4])

o=["venkat"]
k=["isukaplli"]
print(o+k)

