# for single line comment
"""
a=1
"""
# for multiple line comment
print("welcome to starops")
x=2
y=1
z=5 

print(x,y,z)
print(x+y+z)
print(x,y,z,sep="-")
print(x,y,z)
# type conversion:-
a=5
print(type(a))
# " " string
# "5" string
var1="6"
print(type(var1))
var2=int(var1)
print(type(var2))
var3="5"
var5=float(var3)
print(var5)

#bool 
print(bool(34))
print(bool(0))
print(bool(-34))
print(bool("abc"))
print(bool(""))
#ASCII > UTF=>UNICODE TRANSFORMATION FORMAT
#character to Unicode
x="A"
print(ord(x))
#Ord function is used to get the value of character
#Unicode to character
y=65
print(chr(y))
#Chr is used to get the value of numeric to alphabet

#Take input from user
#input function can take at most one argument of str type.
#input always return str type value.
#eg1:-

s=input("Enter your name:\n")
print(type(s))
#how to input an int value
x=int(input("Enter a number:\n"))
print(x)
print(type(x))
a=input("enter")
print(a)
print(type(a))


