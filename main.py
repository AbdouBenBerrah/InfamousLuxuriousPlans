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

  """
#range