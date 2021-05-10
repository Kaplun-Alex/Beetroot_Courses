import timeit
import random as rn


def sorting(a):
    a.sort()
    return a

plot_list_3 = []
count = '100'
for i in range(10):
    t = timeit.timeit('sorting(a)', number=1,
                      setup='import random as rn; a = [rn.randint(1, 3000) for i in range('+count+')]',
                      globals=globals())
    plot_list_3.append(t)
    count = str(int(count)+100)
    print(count)
print(plot_list_3)
