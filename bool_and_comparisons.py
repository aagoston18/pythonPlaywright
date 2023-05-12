print(2 == 2)

# single equals sign is assigning operator a = b
# two equal signs is comparison operator a == b / a != b / a < b / a > b/ a >= b (greater or equal)
# smaller or equal operator
print(2 <= 3)

#compare strings
print("s" == "s")

#string compare is case-sensitiver
print("S" == "s", "will return false")

#compare UTF8 (hex)
print("Alpar"=="alpar")
#python will compare char-by-char and UTF8 hexadecimal values will differ
print("Alpar" < "alpar")

#variables boolean

a = True
b = False

print("a == b is :", a == b)
print("a < b is: ", a < b)
print("a > b is: ", a > b)