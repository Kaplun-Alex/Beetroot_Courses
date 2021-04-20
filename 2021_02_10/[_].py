Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> squares = [1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares+[36,49,64,81,100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cube=[1,8,27,81,125]
>>> 4**3
64
>>> cube[3]=64
>>> cubes
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cubes
NameError: name 'cubes' is not defined
>>> cube
[1, 8, 27, 64, 125]
>>> cube.append(216)
>>> cube
[1, 8, 27, 64, 125, 216]
>>> cube.append(7*3)
>>> cube
[1, 8, 27, 64, 125, 216, 21]
>>> help(append)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    help(append)
NameError: name 'append' is not defined
>>> help(cube.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> help(cube)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> cube.pop()
21
>>> cube
[1, 8, 27, 64, 125, 216]
>>> cube.append(7**3)
>>> cube
[1, 8, 27, 64, 125, 216, 343]
>>> letters=['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5]=['C','D','E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5]=[]
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:]=[]
>>> letters
[]
>>> letters=['a','b','c','d']
>>> len(letters)
4
>>> a=['a','b','c']
>>> n=['1','2','3']
>>> x=[a,n]
SyntaxError: invalid syntax
>>> x==[a, n]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x==[a, n]
NameError: name 'x' is not defined
>>> a
['a', 'b', 'c']
>>> n
['1', '2', '3']
>>> x=[a, n]
>>> n[:]=[]
>>> n
[]
>>> n.append[1,2,3]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    n.append[1,2,3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> n.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    n.append(1,2,3)
TypeError: append() takes exactly one argument (3 given)
>>> n=[1,2,3]
>>> n
[1, 2, 3]
>>> x=[a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> print('з вісутністю пробілу отут x=[a,n] то підступно!  ')
з вісутністю пробілу отут x=[a,n] то підступно!  
>>> 