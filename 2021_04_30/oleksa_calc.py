import argparse

def saver(s, filename, app_d=False):
    print('Result writing in file - ', filename)
    if not app_d:
        f = open(filename, 'w')
        f.write(str(s)+'\n')
    else:
        f = open(filename, 'a')
        f.write(str(s) + '\n')
    f.close()

def max_f(m):
    res = max(m)
    return res

def plus_f(m, s=False):
    if not s:
        res = sum(m)
        return res
    else:
        res = []
        for i in m:
            res.append(str(i)+'+')
        res = ''.join(res)
        all_res = (res[:-1]+'='+str(sum(m)))
        return all_res

def minus_f(m, s=False):
    res = m[0]
    for i in range(len(m)-1):
        res = res - m[i+1]
    if not s:
        return res
    else:
        res_mes = []
        for i in m:
            res_mes.append(str(i)+'-')
        res_mes = ''.join(res_mes)
        all_res = (res_mes[:-1]+'='+str(res))
        return all_res

def mult_f(m, s=False):
    res = m[0]
    for i in range(len(m)-1):
        res = res * m[i+1]
    if not s:
        return res
    else:
        res_mes = []
        for i in m:
            res_mes.append(str(i)+'*')
        res_mes = ''.join(res_mes)
        all_res = (res_mes[:-1]+'='+str(res))
        return all_res

def div_f(m, s=False):
    res = m[0]
    for i in range(len(m)-1):
        res = res / m[i+1]
    if not s:
        return res
    else:
        res_mes = []
        for i in m:
            res_mes.append(str(i)+'/')
        res_mes = ''.join(res_mes)
        all_res = (res_mes[:-1]+'='+str(res))
        return all_res

parser = argparse.ArgumentParser(description='Калькулятор від Олекси')
parser.add_argument('integers', type=int, nargs='+', help='Значення для, кумулятора.')
parser.add_argument('--max', dest='max', action='store_true', help='find the max')
parser.add_argument('--plus', dest='plus', action='store_true', help='sum the integers')
parser.add_argument('--minus', dest='minus', action='store_true', help='minusing of integers')
parser.add_argument('--mult', dest='mult', action='store_true', help='multiplication of integers')
parser.add_argument('--div', dest='div', action='store_true', help='division of integers')
parser.add_argument('-v', dest='v', action='store_true', help='get sintaxis')
parser.add_argument('-f', '--file', dest='f', help='save to file')
parser.add_argument('--append', dest='ap', help='apend result to file', action='store_true')
parser.add_argument('--quiet', '-q', dest='q', help='print- off, save to file - True', action='store_true')
args = parser.parse_args()

if args.max:
    max_op = max_f(args.integers)
    if args.f:
        saver(max_op, args.f, args.ap)
    if not args.q:
        print(max_op)
elif args.plus:
    plus_op = plus_f(args.integers, args.v)
    if args.f:
        saver(plus_op, args.f, args.ap)
    if not args.q:
        print(plus_op)
elif args.minus:
    minus_op = minus_f(args.integers, args.v)
    if args.f:
        saver(minus_op, args.f, args.ap)
    if not args.q:
        print(minus_op)
elif args.mult:
    mult_op = mult_f(args.integers, args.v)
    if args.f:
        saver(mult_op, args.f, args.ap)
    if not args.q:
        print(mult_op)
elif args.div:
    div_op = div_f(args.integers, args.v)
    if args.f:
        saver(div_op, args.f, args.ap)
    if not args.q:
        print(div_op)
else:
    print('no action')


