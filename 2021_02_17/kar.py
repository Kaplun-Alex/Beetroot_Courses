f = open('cmpl.csv', 'r')
t = f.readlines()
f.close()

k = []

for i in t:

    name = i.split(';')[2].lower()
    forb = ('картриджа', 'картриджп', 'лезвие', 'для факс')
    
    if 'картридж' in name:
    
        for j in forb:
            if j in name:
                break
        else:
            k.append(i)
        
f = open('картриджи.csv', 'w')
for s in k:
    f.write(s)
f.close()
        
