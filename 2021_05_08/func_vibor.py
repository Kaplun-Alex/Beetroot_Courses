import timeit
import random as rn

def find_smallest(lst):
    s = lst[0]
    s_index = 0
    for i in range(1, len(lst)):
        if lst[i] < s:
            s = lst[i]
            s_index = i
    return s_index
def sorting(lst):
    new_lst = []
    N = len(lst)
    for i in range(N):
        smallest = find_smallest(lst)
        new_lst.append(lst.pop(smallest))
    return new_lst

plot_list_2 = []
count = '100'
for i in range(10):
    t = timeit.timeit('sorting(lst)', number=1,
                      setup='import random as rn;  lst = [rn.randint(1, 3000) for i in range('+count+')]',
                      globals=globals())
    plot_list_2.append(t)
    count = str(int(count) + 100)
    print(count)
print(plot_list_2)
