import functools as fc
import time

def timer(f):
    @fc.wraps(f)
    def wrap_time(*args, **kwargs):
        start_time = time.perf_counter()
        value = f(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'fin {f.__name__!r} in {run_time:.4f} secs')
        return value
    return wrap_time

@timer
def weistedtraimbratuha(num_times):
    for _ in range(num_times):   # Що б це означало _?
        s = sum([i**2 for i in range(10000)])
        print(s)

weistedtraimbratuha(10)