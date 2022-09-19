#x = "awesome"
#
#def myfunc():
#  x = "fantastic"
#  print("Python is " + x)
#myfunc()
#print("Python is " + x)

#---------------------------------------------
#putting global followed by a variable changes that variable to the global variable.
#x = "awesome"
#
#def myfunc():
#  global x
#  x = "fantastic"

#myfunc()
#print("Python is " + x)

#This makes x="fantastic the global var"

# Or when theres a var in a func you want to make global.

#def myfunc():
#  global x
#  x = "fantastic"
#
#myfunc()
#
#print("Python is " + x)


#----------------------------------------------------------
x = "Jojo's Bizzare Adventure"

def myfunc():
    global x
    x = "Tokyo Ravens"
    print("The best anime is," + x)
myfunc()
print("The best anime is," + x)
print("The best anime is," + x)

#---------------------------------------------