x = "Hello World"
def myfunc():
    global x
    x = "Hello World"
    print(x)
myfunc()
print(x + ", Good Morning")

##x = "Jojo's Bizzare Adventure"
##def myfunc():
##    x = "Tokyo Ravens"
##    print(x)
##myfunc()
##print(x + "is mid bro")


#-----------------------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print (thisdict)

#---------------------------------------


for x in thisdict:
  print(x)
#-----------------------------------------

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#if statements---------------------------------
a = 33
b = 200
if b < a:
  print("b is less than a") #indentation
elif b == a:
    print("b is equal than a") #"if the previous conditions were not true, then try this condition".
else:
    print("b is greater than a") 

    #else--------------------------------
a = 33
b = 200
if b < a:
  print("b is less than a") #indentation
else:
    print("b is greater than a") 



#shorthand
if a > b: print("a is greater than b")

a = 10
b = 20 

print("Yes") if a > b else print("NO")

#------------------------------------------------------------
a = 100 
b = 200 

print("A") if a > b else print("=") if a == b else print("B")


#AND operator 
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


#Or operator
a = 200
b = 33
c = 500

if a > b or a > c:
  print("At least one of the conditions is True")



#Nested If statement 
x = 41

if x > 10:
    print("> than 10")
    if x < 45:
     print("also < 50")
    else:
     print("not above 20") 

    
#--------------------------------------
x = 30
y = 30

if x > y:
  print("Greater")
#elif x == y:
#  print("Equal")
#else:
#  print("Lesser")
while x == y:
  print("Equal")
  x += 3
else:
  print("Lesser")

###---------Loops
##i = 1
##while i < 6:
##  print(i)
##  i += 1
##else:
##  print("i is no longer less than 6")