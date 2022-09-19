class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))

#--------------------------------------------------------#
thislist = ["apple", "banana", "cherry"]
print(thislist)

list1 = ["abc", 34, True, 40, "male"]
print(list1)


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
print(thislist[2:6])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, ' apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[2] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

myset = {"apple", "banana", "cherry"}
print(type(myset))


