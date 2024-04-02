import functools
def print_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'args={args}')
        print(f'args={kwargs}')
        result = func(*args, **kwargs)
        print(f'result={result}')
        return result
    return wrapper

def sum_list(func):
    @functools.wraps(func)
    def wrapper(a, b):
        c = list()
        for x in range(0,len(a)):
            c.append(a[x] + b[x]) 

        return c
    return wrapper


@sum_list
def sum(a,b):
    return a+b

res = sum([1,2,3],[1,2,3])
print(res)