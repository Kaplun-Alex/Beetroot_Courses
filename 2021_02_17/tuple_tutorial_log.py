Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=12345,54321,'hello!'
>>> t[0]
12345
>>> t[2]
'hello!'
>>> t
(12345, 54321, 'hello!')
>>> u=t,(1,2,3,4,5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> t[0] =888889
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t[0] =888889
TypeError: 'tuple' object does not support item assignment
>>> v=([1,2,3,],[3,2,1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> empty=()
>>> len(empty)
0
>>> singelton= 'hello'
>>> len(singelton)
5
>>> tuple(singelton)
('h', 'e', 'l', 'l', 'o')
>>> singelton
'hello'
>>> singelton='hello',
>>> len(singelton)
1
>>> singelton
('hello',)
>>> x,y,z=t
>>> x
12345
>>> y
54321
>>> z
'hello!'
>>> 