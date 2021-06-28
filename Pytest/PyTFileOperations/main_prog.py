def open_and_modyfy(file_nm):
    f = open(file_nm, 'r')
    t = f.readlines()
    f.close()
    return t

