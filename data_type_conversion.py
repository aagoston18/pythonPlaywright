integer = 12
string = "text"
float = 1.2345

print(f'{integer}')

#printing two strings will NOT perform math operations
print ('1' + '1') #output will be 11, not two as it will concatinate the two strings

#print math on string and int datatypes
# print ('1' + integer) #will throw type error #TypeError: can only concatenate str (not "int") to str

#casting
#
# string to int using internal int() function
print(int("2") + int("2"), "...will results in 4 ") #will result in 4

#int to string using str()

a = 123
b = 321
print(a + b, "...will perform the math because variablese a and b are integers")
print(str(a) + str(b), "...will contatinate two strings instead of performing math operation")