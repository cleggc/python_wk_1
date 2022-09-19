#data types
name ="Jon"
age = 22
height = 187.5
f_foods = ["jollof", "chicken stew", "pounded yam"]

print(type(name))
print(type(age))
print(type(height))
print(type(f_foods))

print('Hello, World')

#Indentations represent a new block of code
x = 1
if x == 1:
 print("x is 1.")
breakpoint
if 5 == 2:
 print("5 is > than 2")
#--------------------------------------------------
#Easy aggregation 
x = 5
y = 6
print(x + y)

x = 4
y = 5
X = 20
print ((X/x)*y)

if 25/5 == 5:
 print('True')


#------------------------------------------
#Type() can tell you the data type of a variable
x = 5
y = 'John'
print(type(x))
print(type(y))

#------------------------------
#Variable names are case-sensitive

x = 4
y = 5
X = 20
print ((X/x)*y)


#----------------------------------------------
#Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#---------------------------------------------------

anime_collection_count = [22, 32, 45]
manga = [1, 2, 3]
x,y,z = manga
a,b,c = anime_collection_count
if x+y+z < a*b*c:
    print('Amen')

#---------------------------------------------------

x = "Jojo's Bizzare Adventure,"
y = "One Piece,"
z = "Black Bullet"

print(x,y,z)


x = "Jojo's Bizzare Adventure"
y = "is,"
z = 7
X = "out of"
Y = 10
print(x,y,z,X,Y)

#-------------------------------------------------
#Global functions
x = "Jojo's Bizzare Adventure"

def myfunc():

    print(x + "is mid bro")
myfunc()



x = "Jojo's Bizzare Adventure"

def myfunc():

    x = "Tokyo Ravens"

    print(x + "is mid bro")

myfunc()
print(x + "is mid bro")
#---------------------------------------------

x,y,z = [1,2,3]
a,b,c = [4,5,6]
q = z*z 
w = a+b
def func():
 if y*z > b:
    print(q/w)

func()
#------------------------------------------------
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
print("Python is " + x)
myfunc()
print("Python is " + x)

