def siko_zminnuh():
    i = 0
    l = ['l']
    d = {1:'d'}
    s = {'s', 'e', 't'}
    k = ('k', 0, 'r', 't')
    print(i, l, d, s, k)

siko_zminnuh()
sz = siko_zminnuh
print(sz.__code__.co_nlocals)
