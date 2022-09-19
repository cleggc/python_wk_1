x = "JoJo is the swag God"
#print(len(x))
print(x[:5])


x = "JoJo is the swag God"
#print(len(x))
print(x[2:])

x = "JoJo is the swag God"
#print(len(x))
print(x[2:])

x = "JoJo is the swag God"
#print(len(x))
print(x[2:10])

x = "JoJo is the swag God"
#print(len(x))
print(x[-5:-2])

b = "Hello, World!"
print(b[-5:-2])


#--------------------------------------------#
x = "JoJo is the swag God"
print(x.upper())

x = "JOJO IS A KING OF SWAG"
print(x.lower())

x = " JJ is the king of swagg  "
print(x.strip())
#---------------------------------------------------------
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#------------------------------------------------------------
#-----format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



age = 23
day = 14
month = 9
year = 1999
txt = "I am {0}, I was born on the {1}/{2}/{3}"
print(txt.format(age,day,month,year))
#--------------------------------------------------------------------#
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#----------------------------------------------------------------------
#Booleans

x="Today is sunny"
y="Today is wet"

if len(x) > len(y):
    print("YES")
else:
    print("NO")


x = ""
y = 0

print(bool(x))
print(bool(y))