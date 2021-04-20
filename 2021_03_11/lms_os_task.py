def read_symbols(cr):
    f = open(cr, 'r', encoding='utf8')
    tr = len(f.read())
    print('Кількість символів', tr)
    return tr


def read_rows(cr):
    f = open(cr, 'r', encoding='utf8')
    tl = len(f.readlines())
    print('Кількість строк', tl)
    return tl


def all_of(cat_rez):
    rs = read_symbols(cat_rez)
    rr = read_rows(cat_rez)
    return rs, rr
