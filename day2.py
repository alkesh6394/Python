# #various operator in python
# #a)airthmetic operator
# # //,/,+,-,*,%
# #// floor
# print(15//4.0)
# #/ true division
# print(15/4.0)
# #%
# print(15%4)
# print(4*"abc")
# #b)Realational operator
# #<,>,=,==,<=,>=,!=
# # Realtional operator always give result in True or false 
# #when truth value is convert to int it become 1 for the true and 0 for the false
# print(5==5)
# print(int(True))
# #c)Logical operator
# '''
# AND
# True and True=True
# T and F=false
# f and t=False
# OR
# F or f=f
# f or t= true
# t or f =true
# not
# not true=false
# not false=true
# '''
# #d)Bitwise Operator
# '''
# &(and),|(or), ^(xor),~(not) ,>>(right shift),<<(left shift)
# 0 & 0=0
# 0 & 1=0
# 1 & 0=0
# 1 & 1=1


# 0|0=0
# 0|1=1
# 1|1=1
# 1|0=1

# 0^0=0
# 0^1=1
# 1^0=1
# 1^1=0
# '''
# print(~101)
# print(25 & 37)
# print( 44 | 71)
# print(56^29)


# #f)Membership operator
# #g)Addition opeartor
# a="alkesh "
# b="dewang"
# print(a+b)
# #Assignment Operator
# # x=1
# # x+=5=x=x+5
# # x*=2=x=x*2
# x,y,z=2,1,5


#e)Identity opeartor

b=35
c=45
print(c is not b)


#Decision control

# if
# if else
# if elif elif else

# write a program to check a number is positive or not?

x=int(input("Enter a number:\n"))
if x>0:
    print("positive")
else:
    print("negative")

if condition:
    ---------
    ---------
elif condition:
    ----------
    ----------
elif condition:
    ---------
    ---------
else:
    ---------
    ---------

