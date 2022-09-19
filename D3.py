#python casting, there may be times when you want to specify a type on to a variable


#int will make a sting or float into a whole number
from re import A


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3 

#print(x)
#print(y)
#print(z)

#float will make an int, string into a float/ decimal 
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#print(x)
#print(y)
#print(z)
#print(w)

#string will make an int or float into a string
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#print(x)
#print(y)
#print(z)
##----------------------------------------------------------------
#
x = float(1)  
y = str(2.0) 
z = int("3")
a = x+z

def myfunc():
  global a
  a = 5
#print(a)
myfunc()

#print(a)

#----------------------------------------------------------------
#strings are arrays, this example is the alphabet which generally has 26 letters but arrays start from 0. Hence why in this example there are [25] characters in the array. [0-25]
#the inputted array number in the print statement will output the character in that position. 

z = "abcdefghijklmnopqrstuvwxyz"
print(z[1])
#lets you check the length of a string 
print (len(z))


#loops, since strings are arrays we can loop through the characters in a string, using for
for z in "abcdefghijklmnopqrstuvwxyzzzzzzzzzz":
    print(z)
   

# in function to check a string 
txt = "The best things in life are free!"
print("freiie" in txt)
print("best" in txt)
#-------------------------------------------------------------------

x = "The weather is good"
y = "The weather in bad"
if len(x) > len(y):
    print("yes")


