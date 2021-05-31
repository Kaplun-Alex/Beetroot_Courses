import sys

c = sys.argv[1:]

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
    
print(s)
