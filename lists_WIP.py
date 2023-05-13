#list are created using square brackets sign
#lists in python start with 0
a = []
b = [10, 1, 2, 3, 4, 5]
c = [ 9 , 8, 7, "hello", 1.23, 3.456]

print(a)
print(b)
print(c)

#List operations
#index
print(b.index(10))
print(c.index("hello"))
print(c.index(3.456))

#revers - reverses all values in the list
print(b.reverse())
print(b)

#pop - removes the last value of the list by default or by given index
print(c.pop())
print(c)
print(b.pop(0))
print(b)

#append - adds items to the list
print(a.append(99))
print(a)

#count - returns number of occurances of given value in the list
print(a.count(0))
print(a.count(99))