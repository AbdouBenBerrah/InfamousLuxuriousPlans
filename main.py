# Fundamental Data Types 
# int and float

# print(type(2+6)) 
# print (2**4) # to the power = 16
# print(11//4) # int division result = 2 
# print(7%4) # remainder of int div = 3

# maths functions

# # print(round(3.1))
# print(abs(-20))

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# augmented assigment operator

# some_value = 5
 # some_value += 2
 # some_value -= 3
 # some_value *=2


# Strings

##      'this is a string'
#       "this is also a string"

# formatted strings

#name = 'Abdou'
#age = 40
#print('Hi {name}. You are {age} years old')

#sentence = 'a list of letters'
#print(sentence)
#print(sentence[:4])
#print(sentence[4])
#print(sentence[4:8])
#print(sentence[8:])

# string concatenation

#st1 = "hello"
#st2 = "there"
#print(st1 +' '+ st2)
#print(st2 +' '+ st1 + str(     100))
#print(st2 +' '+ st1 +' '+ str(100))

# escape sequences
# weather1 = 'it\'s sunny today\n'
# weather2 = "it's sunny today\n"
# weather3 = "it's \"kind of sunny\""
# print(weather1, weather2, weather3)
# \t = tab , \n = new line 

# formatted strings
#name = 'John'
#age = 20
#print('Hi ' + name + '. you are ' + str(age) + ' years old' )

#print(f'Hi {name}. You are {age} years old')

sentence = 'a list of letters'

#print(sentence[-2])
######################## string slicing    [start:stop:stepover]
#print(sentence[0:10:2])
#print(sentence[::-1])  # reverse the string
#print(sentence[::-2])

###  immutability

### built-in functions

#print(len(sentence))

# strings methods

#print(sentence.upper())
#print(sentence.capitalize())
#print(sentence.find('l'))
#print(sentence.count('l'))
#print(sentence.replace('l', 'P'))

# booleans
#is_cool = False
#is_cool = True
#print(bool(0))
#print(bool(1))
#print(bool(4))
#print(bool('False'))
#print(bool(''))
#print(bool(' '))

#birth_year =int(input('what year were you born ?'))

#age = 2020 - birth_year
#print(f'your age is {age}')

# password check

#username = input('enter your username :')
#pwd = input('enter password :')
#lenpwd = len(pwd)
#hidpwd = '*' * lenpwd

#print(f'Hello {username}, your password {hidpwd} is {str(lenpwd)} letters long ' )

#########         LISTS

shop_cart = [
  'food',
  'other',
  'toys',
  'sunglasses'
  ]
#print(shop_cart[0])

### list slicing

#print(shop_cart[1:3])
#print(shop_cart[0::2])

# list modification   mutability

#shop_cart[0] = 'drinks'
#print(shop_cart)
#new_cart = shop_cart[:]  # copy the content of a list 
                        # new_cart = shop_cart is memory pointing
                        # change on new_cart will affect shop_cart
#new_cart[0] = 'gum'
#print(new_cart)
#print(shop_cart)


######## Matrices

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
#print(matrix)
#print(matrix[0][1])

#######   LISTS METHODS

basket=[1,2,3,4,5]
#print(len(basket))     ## built-in function

### adding methods
new_list = basket.append(100)
#print(basket)  ## prints Basket
#print(new_list)  # prints None   .append does not produce a new value

basket.insert(3, 99)
#print(basket)

basket.extend([100,101])
#print(basket)


#### removing methods

basket.pop()
#print(basket)

basket.pop(0)   ### remove at index
#print(basket)

basket.remove(99)   ### remove value
#print(basket)

new_list2 = basket.pop(4)
#print(new_list2)

#basket.clear()   # -> []
#print(basket)

#print(basket.index(2))    # gives index of value '2'

#print('d' in basket)  # gives boolean

#print(basket.count(2))
basket.sort()
x = sorted(basket)
#print(basket)
#print(x)
x.reverse()
#print(x)

##### common list patterns

basket.sort()
basket.reverse()
#print(len(basket))
#print(basket[::-1])
#print(basket)

#print(range(1,100))
#print(list(range(100)))

#new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Bobo'])
#print(new_sentence)

##### list unpacking
#a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
#print(a)
#print(b)
#print(c)
#print(other)
#print(d)


#######    None
#weapons = None
#print(weapons)


######## Dictionary  dict

dictionary = {
  'a': [1,2,3],
  'b': 'hello',
  'x': True
}

#print(dictionary['b'])
#print(dictionary)
#print(dictionary['a'][1])

my_list = [
  { 'a': [1,2,3],
    'b': 'hello',
    'x': True
},
{
  'a': [4,5,6],
  'b': 'hello',
  'x': True
}
]
#print(my_list[1]['a'][2])

##### Dictionaries Methods

user = {
  'name': 'Dadi',
  'age' : 45
}

#print(user.get('deathage', 55))

user2 = dict(name='Dada', age='30')
#print(user2)


#print('basket' in user.keys())
#print('basket' in user.values())
#print(user.items())
#user.clear()
#print(user)

user2 = user.copy()
#print(user2.pop('age'))
#print(user2)

#print(user.popitem())
#print(user)

#print(user.update({'age':55}))
#print(user)
#print(user.pop('age'))


######## TUPLES

my_tuple = (1,2,3,4,5,5,5,5)

#print(my_tuple[1])
#print(5 in my_tuple)

user = {
  (1,2):[1,2,3],
  'greet':'hello',
  'age':20
}

#print(user.items())
#print(user[(1,2)])

new_tuple = my_tuple[1:2]
#print(new_tuple)
new_tuple = my_tuple[1:4]
#print(new_tuple)

x,y,z,*other = (1,2,3,4,5)
#print(x)
#print(other)

#######  Tuples Methods

#print(my_tuple.count(5))
#print(my_tuple.index(4))
#print(len((my_tuple)))


######### SETS  unoredred collection of unique objects


my_set={1,2,3,4,5,5}   
#print(my_set)    # no duplicates
my_set.add(100)
my_set.add(2)
#print(my_set)

my_list=[1,2,3,4,5,5,5]
# how to return a list without repetition
#print(set(my_list))

#print(1 in my_set)
#print(len(my_set))
#print(list(my_set))

new_set = my_set.copy()
my_set.clear()
#print(new_set)
#print(my_set)

########### SETS METHODS   

my_set={1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

#print(my_set.difference(your_set))

my_set.discard(5)
#print(my_set)

#print(my_set.difference_update(your_set))
#print(my_set)

#print(my_set.intersection(your_set))
#print(my_set.isdisjoint(your_set))
#print(my_set.union(your_set))
#print(my_set.issubset(your_set))
#print(my_set.issuperset(your_set))
#print(my_set | your_set)  # union
#print(my_set & your_set)  # intersection

###########################################################################
###########################################################################
############### Python Basics 2


###### Conditional logic

#is_old = False
#is_licenced = True

#if is_old:
#  print('you are old enough to drive!')
#elif is_licenced:
#  print('you can drive!')
#else:
#  print(' too young to drive!')


####### Ternary operator
#is_friend = True
#can_message = "message allowed" if is_friend else "not allowed to message"
#print(can_message)


######## short circuiting

#is_user = True

#if is_friend and is_user :
  #print('best friends forever')

#if is_friend or is_user :
  #print('friends ')

#######  logical operator

# and
# or
# < <=
# > >=
# == is equal ####  === is identic    #### != not equal  #### <> 
"""
+=	    x += 5	        x = x + 5
-=	    x -= 5	        x = x - 5
*=	    x *= 5	        x = x * 5
/=	    x /= 5	        x = x / 5
%=	    x %= 5	        x = x % 5
//=	    x //= 5	        x = x // 5
**=	    x **= 5	        x = x ** 5
&=	    x &= 5	        x = x & 5
|=	    x |= 5	        x = x | 5
^=	    x ^= 5	        x = x ^ 5
>>=	    x >>= 5	        x = x >> 5
<<=	    x <<= 5	        x = x << 5

####### #######    Exercise

is_magician = True
is_expert = True

if is_magician and is_expert:
  print("you are a master magician")
elif is_magician and not is_expert:
  print("at least you're getting there")
elif not is_magician:
  print("you need magic powers") 


#########  FOR LOOPS


def isPalindrome(s):
  return s==s[::-1]

word = "malayalam"
ans = isPalindrome(word)
if ans :
  print("Yes")
else:
  print("No") 


#########  FOR LOOPS

### for some_item in some_iterable:
    #### do something
#strings
for letter in 'zero to mastery':
  print(letter)
#lists
for item in [1,2,3,4,5]:
  print(item)
#tuple
for item in (1,2,3,4,5):
  print(item)
#set
for item in {1,2,3,4,5}:
  print(item)



#nested loops
for item in (1,2,3,4,5):
  for x in ['a','b','c']:
    print(item,x)
    

 
# dictionary

user = {
  'name': 'Mohamed',
  'age':35,
  'can_swim':True
}

for item in user:
  print(item)

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for key, value in user.items():
  print(key, value)



# counter exercise

my_list = [1,2,3,4,5,6,7,8,9]
counter = 0
for item in my_list:
  counter+= item

print(counter)

  
#range

print(range(100))
for _ in range(0,100,2):
  print(_, range(100))


for _ in range(10):
  print(list(range(10)))



# enumerate 

for char in enumerate('Hellllllooo'):
  print(char)

for i,char in enumerate('Hellllllooo'):
  print(i,char)

for i,char in enumerate((1,2,3,4)):
  print(i,char)



for i,char in enumerate(list(range(100))):
  print(i,char)
  if char ==50:
    print("index of 50 is :", i)


# while loops

i = 0
while i < 50:
  print(i)
  i+=1


while True:
  input('say something: ')
  break

while True:
  response = input('say something: ')
  if (response == 'bye'):
    break
   # continue go back to the Loop
   # pass placeholder, prevent a bug in empty loops


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# iterate over picture
  ## if 0 print ' '
  ## if 1 print '*'

for row in picture:
  for pixel in row:
    if pixel == 0 :
      print(' ', end='')
    else:
      print("*", end='')
  print('')



## exercise check for duplicate in list

a_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates =[]
for value in a_list:
  if a_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)




#### Functions

def say_hi():
  print('Hi')

say_hi()
#print(say_hi)

#parameters
#positional parameters

def say_hello(name, emoji):
  print('Hello', name , emoji )

#arguments actual values we provide to functions
#positional arguments
say_hello('Abdou', '😀')
say_hello('Moh', '😀')
say_hello('Emily', '😀')

# keyword arguments 

say_hello(emoji='☹️', name='Baba')

# default parameters

def greet(name='Darth Vader', emoji='😈'):
  print('Hello', name, emoji)

greet('Luke', '😀')
greet()

# return

def sum(num1, num2):
  return num1+num2

total = sum(4,5)
print(total)


# methods Vs functions

#'hello'.

# docstrings  describing the function job

def test(a):
  '''
  Info : this function tests and prints param a 
  '''
  print(a)

test('9999')

##magic methods

print(test.__doc__)



# clean code 
def is_even(num):
  return num % 2 == 0
    
print(is_even(50))
print(is_even(51))



###  *args **kwargs

def super_func(*args, **kwargs):
  print(*args)
  print(kwargs)
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4, num1 = 5, num2 = 10)) 



# exercise function

def highest_even(li):
  highest = 0   # evens =[]
  for item in li:
    if item % 2 == 0:
      if item >highest:  # evens.append(item)
        highest = item
  
  return highest # return max(evens)



print(highest_even([15,10,3,4,6,8,12]))



## Scopes

total = 0
def count():
  global total  # use the global total instead of creating a new one inside the function's scope
  total +=1
  return total

count()
count()
print(count())

## dependency injection

total = 0
def count(total):
  total +=1
  return total

print(count(count(count(total))))


### nonlocal keyword

def outer():
  x = "local"
  def inner():
    nonlocal x
    x = "non local"
    print("inner:", x)
  
  inner()
  print("outer:", x)

outer()



###### OOP

class BigObject:
  pass

obj1 = BigObject()

print(type(BigObject))
print(type(obj1))


class PlayerCharacter:
  
  membership = True  # Class Object Attribute
  def __init__(self, name, age):    
    if self.membership :
      self.name = name  # dynamic object attributes
      self.age = age
  def shout(self):
    print(f'my name is {self.name}')
  def run(self):
    print('Run')
    return 'done'
  
  ### decorators

  @classmethod      ### mwthod on class doesnt need to instantiate objects to use class method
  def adding_things(cls, num1, num2):      # cls class equivalent to self
    #return num1 + num2
    return cls('Teddy', num1+num2)

  @staticmethod   # no access to cls, to use  when we don't care about attributes
  def adding_things2(num1, num2):
    return num1 + num2
  

  
  
player1 = PlayerCharacter('Aaa', 33)
player2 = PlayerCharacter('Bbb', 44)

#print(player1.name)
#print(player1.age)
#print(player1.run())
#print(player1.shout())
#print(player2.shout())


# help(list)

#print(player1.adding_things(2,3))
player3 = PlayerCharacter.adding_things(2,3)
#print(player3)
print(player3.age)


class NameOfClass():
  class_attribute = 'value'
  def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2

  def method(self):
    #code
  
  @classmethod
  def clas_method(cls, param1, param2):
    # code  
  
  @staticmethod
  def static_method(param1, param2):
    # code 
    

#### 4 pillars of OOP
### Encapsulation   : bonding of data and functions ( attributes and methods)
### Abstraction

class PlayerCharacter:
  
  def __init__(self, name, age):    
    self._name = name  # _ indicates it should not be modified
    self._age = age    #   treated as private

  def run(self):
    print('run')
  
  def speak(self):
    print(f'my name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('Abdou', 100)
player1.speak()  # we don't need to know how speak() works to use it

# player1.name = '!!!!!'  # still can modifiy attributes
# player1.speak = 'Boooooo'   # and even methods , no real privacy in Python

# print(player1.speak)

####### INHERITENCE
#  allows new objects to take properties of existing objects

class User:
  def sign_in(self):
    print('logged in')

class Wizard(User):  # pass the parent class that we want to inherit
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, nb_arrows):
    self.name = name
    self.nb_arrows = nb_arrows
  
  def attack(self):
    print(f'attacking with arrows: arrows left-{self.nb_arrows}')
  

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
#rint(wizard1.sign_in())
#print(archer1.sign_in())
wizard1.attack()
archer1.attack()

# isinstance(instance, class) 
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))


########## POLYMORPHISM
#####  method belong to objects
#####  object classes can share the same method Name
#####  method names can act differently based on what object calls them

class User:
  def sign_in(self):
    print('logged in')

  def attack(self):
    print('Do Nothing')

class Wizard(User):  # pass the parent class that we want to inherit
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):   ## attack is defined for both subclasses
    User.attack(self)   # use the attack method from parent
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, nb_arrows):
    self.name = name
    self.nb_arrows = nb_arrows
  
  def attack(self):  ### but this one acts differently from wizard attack
    print(f'attacking with arrows: arrows left-{self.nb_arrows}')
  

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

print(wizard1.attack())

#wizard1.attack()  
#archer1.attack()    ## output is different because object caller is 

def player_attack(char):
  char.attack()

#player_attack(wizard1)  # again same function different output
#player_attack(archer1)

#for char in [wizard1, archer1]:
 # char.attack()


##### super()

class User(object):
  def __init__(self, email):
    self.email = email
  
  def sign_in(self):
    print('logged in')


class Wizard(User):  
    def __init__(self, name, power, email):
      #User.__init__(self, email)
      super().__init__(email)  # refer to parent class
      self.name = name
      self.power = power

    def attack(self):  
      print(f'attacking with power of {self.power}')


  

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')

print(wizard1.email)


###### Object Introspection
### ability to determine type of object during Runtime

class User(object):
  def __init__(self, email):
    self.email = email
  
  def sign_in(self):
    print('logged in')


class Wizard(User):  
    def __init__(self, name, power, email):
      #User.__init__(self, email)
      super().__init__(email)  # refer to parent class
      self.name = name
      self.power = power

    def attack(self):  
      print(f'attacking with power of {self.power}')


  

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
#print(dir(wizard1.email))
print(dir(wizard1))  # dir function  gives all methods and attributes of instance wizard1


###### Dunder Methods

class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age 

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))   




# Exercise Extending list

class SuperList(list):
  def __len__(self):
    return 1000


super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])

print(issubclass(SuperList, list))



#### multiple INHERITENCE

class User(object):
  def __init__(self, email):
    self.email = email
    print('init complete')
  
  def sign_in(self):
    print('logged in')


class Wizard(User):  
    def __init__(self, name, power):
      self.name = name
      self.power = power

    def attack(self):  
      print(f'attacking with power of {self.power}')
    

class Archer(User):
  def __init__(self, name, nb_arrows):
    self.name = name
    self.nb_arrows = nb_arrows
  
  def check_arrows(self): 
    print(f'{self.nb_arrows} left-')
  
  def run(self):
    print('run')

class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, nb_arrows):
    Archer.__init__(self, name, nb_arrows)
    Wizard.__init__(self, name, power)



wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

hb1 = HybridBorg('borgie', 50, 100)

#print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())


##### MRO Method Resolution open

class A:
  #num = 10
  pass

class B(A):
  pass

class C(A):
  #num = 1
  pass

class D(B, C):
  pass

#print(D.num)
print(D.mro())
# D.num
D.__str__



class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass 
class M(B, A, Z): pass

print(M.mro())




##########################################
######### Functional Programming

## map() , filter(), zip(), reduce()

from functools import reduce

my_list = [1,2,3]
def multiply_by_2(item):
  #new_list = []
  #for item in li:
   # new_list.append(item*2)
  #return new_list
  return item*2   # replace code above with use of map

#print(list(map(multiply_by_2, my_list)))
#print(my_list)

def only_odd(item):
  return item % 2 != 0

#print(list(map(only_odd, my_list)))
#print(list(filter(only_odd, my_list)))
#print(my_list)

your_list=[10,20,30]
your_tuple=(40,50,60)
#print(list(zip( my_list, your_list)))
#print(list(zip( my_list, your_list, your_tuple)))

#print(my_list)

def accumulator(acc, item):
  print(acc, item)
  return acc + item

#print(list(reduce(accumulator, my_list, 0)))
#print(reduce(accumulator, my_list, 0))
#print(my_list)

##################### Lambda expressions

### anonymous function you only need oct

## lambda param: action(param)



print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item%2 !=0, my_list)))
print(reduce(lambda acc,item: item+acc, my_list))

print(my_list)


####### exercise lambda expressions

my_list = [5,4,3]

print(list(map(lambda item: item**2, my_list)))

a = [(0,2), (10,-1), (9,9),(4,3) ] 

# list sorting
a.sort(key=lambda x: x[1])  # i want to sort by the key which is 2nd item
print(a)
#print(list(filter(lambda item: )))



##################  List, Set, dictionary comprehensions
my_list = []

for char in 'hello':
  my_list.append(char)

#print(my_list)

#### same code with comprehensions
my_list2 = [char for char in 'hello']
#print(my_list2)

my_list3 = [num for num in range(0,100)]
#print(my_list3)

my_list4 = [num*2 for num in range(0,100)]
#print(my_list4)

my_list5 = [num**2 for num in range(0,100) if num%2==0]
#print(my_list5)


my_set = {char for char in 'hello'}
#print(my_set)

my_set2 = {num for num in range(0,100)}
#print(my_set2)

my_set3 = {num**2 for num in range(0,100) if num%2==0}
#print(my_set3)

my_dict= {
  'a':1,
  'b':2,
  'c':3
}
my_dict2 = {key:value**2 for key, value in my_dict.items() if value%2==0}
print(my_dict2)

my_dict3 = {num:num*2 for num in[1,2,3]}
print(my_dict3)


###################   Exercise comprehensions
sm_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([char for char in sm_list if sm_list.count(char) > 1 ]))
print(duplicates)
"""

######################## Decorators

#def hello():
 # print('hello')
#
#greet = hello
#hello()
#del hello    # delete the pointer hello but the function still works
#print(greet())

#def hello(func):
 # func()

#def greet():
  #print('still here')

#a = hello(greet)  # we call function hello with argument function greet
#print(a)

########## Higher order function HOC
### any function that accept a function as a parameters
### or return a function

def greet(func):
  func()

def greet2():
  def func():
    return 5
  return func

#### a decorator enhance and supercharge a function

def my_decorator(func):
  def wrap_func():
    print('*************')
    func()
    print('*************')
  return wrap_func

@my_decorator
def hello():
  print('hello')

hello()

