thisdict = {
    "Model": "Camry",
    "Available": "2009",
    "price": 600000000
}
x = {
    "Mercedes":  "C300",
    "available": "2021",
    "price": 210000000
}
print(thisdict)
thislist = list(("Ford","Camry", "Mercedes"))
newlist = ["Audi", "BMW", "Fortuner"]
newlist.append(thislist)
print(newlist)
for x in thislist:
    print(x)
if "Ford" in thislist:
    print("Yes, Ford is exist")
else:
    print("no, Ford is not exist")  


class Person:
  def __init__(self, characteristic, nationality):
   self.characteristic = characteristic
   self.nationality = nationality
    
  def printname(self):
    print(self.characteristic, self.nationality)
class Student(Person):
    def __init__(self, characteristic, nationality):
        Person.__init__(self, characteristic, nationality)
x = Student("friendly", "American")
x.printname()

def tri_recursion(k):
  if (k > 0):
      result = k + tri_recursion(k-1)
      print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results:")
tri_recursion(6)

mystr = "lamboghini"
myitr = iter(mystr)

print(next(myitr))    
print(next(myitr)) 
print(next(myitr)) 
print(next(myitr)) 
print(next(myitr))     
print(next(myitr)) 
print(next(myitr)) 


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)     

# Modules
def greeting(name):
    print("Hello" + name)
import app
app.greeting("Minh Dinh")

information = {
    "name" : "Minh Dinh",
    "age": 16,
    "school": "CSP"
}
import app
a = app.information
print(a)

import platform # Checking types of device
x = platform.system()
print(x)

import platform # Checking version
y = dir(platform)
print(y)

import datetime
a = datetime.datetime.now()
b = datetime.datetime(2021,5,17)
print(a)
print(b)

# Math
z = min(25,15,50)
l = max(25,29,30)
print(z,l)

o = abs(-10)
print(o)

p = pow(5,3)
print(p)

import math
r = math.sqrt(100)
print(r)

import math
k = math.ceil(1.4) #2
g = math.floor(1.4) #1
print(k)
print(g)

import json
f = '{"name": "mD", "age": 16, "school": "CSP"}'
u = json.loads(f)
print(u["age"])

#Convert python into json
import json 
dict1 = {"type": "Diagram",
        "Words limit": 150,
        "requirement":"depict all"
}
t = json.dumps(dict1)
print(t)

# Regeg function
import re 
txt = "The rain in Hanoi"
x = re.search("^The.*Spain$",txt)
if x:
    print("Yes, it exists!")
else:
    print("No, it doesn't exist!")

import re 
txt = "The rain in Hanoi"
x = re.findall("ai",txt)
print(x)

import re

txt = "The rain in Spain"
w = re.search("\s", txt)

print("The first white-space character is located in position:", w.start())

import re

txt = "The rain in Spain"
ab = re.split("\s", txt)
print(ab) #['The', 'rain', 'in', 'Spain']

#The sub() Function
import re

txt = "The rain in Spain"
rt = re.sub("\s", "9", txt)
print(rt) #thay space bằng số 9

import re

txt = "The rain in Spain"
bt = re.sub("\s", "9", txt, 2)
print(bt) #thay space bằng 2 số 9

import re

txt = "The rain in Spain"
xy = re.search(r"\bS\w+", txt)
print(xy.span())

import re
#The string property returns the search string:
txt = "The rain in Spain"
xh = re.search(r"\bS\w+", txt)
print(xh.string)

#Print the part of the string where there was a match.

#vThe regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
xq = re.search(r"\bS\w+", txt)
print(xq.group())


try:
  print(j)
except:
  print("An exception occurred")

try:
  print(m)
except NameError:
  print("Variable m is not defined")
except:
  print("Something else went wrong")  

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(cv)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

# xd = -1
# if xd < 0:
 # raise Exception("Sorry, no numbers below zero")

# xj = "hello"
# if not type(xj) is int:
  # raise TypeError("Only integers are allowed")  

# username = input("Enter username:")
# print("Username is" + username)

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print('2nd elements on 1st array:' ,arr[0,1])
