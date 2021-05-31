import sys

c = sys.argv[1:]

if '-v' in c:
    verb = True
    c.remove('-v')
else:
    verb = False

op = c.pop()
s = 0


    
op1 = float(c[0])
op2 = float(c[1])

if op == '+':
    s = op1 + op2
elif op == '-':
    s = op1 - op2
elif op == '*':
    s = op1 * op2
elif op == '/':
    s = op1 / op2
else:
    print('Что-то пошло не так')

if verb:
    print(f'{op1} {op} {op2} = {s}')
else:
    print(s)


