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
    def wrapper(*args, **kwargs):
        if len(args) !=2:
            raise ValueError('Must be 2 lists')
        if type(args[0]) == int:
            return func(*args,**kwargs)
        if len(args[0]) != len(args[1]):
            raise ValueError('Lists has different length')
        c = list()
        for x in range(0,len(args[0])):
            c.append(func(args[0][x], args[1][x])) 

        return c
    return wrapper

@sum_list
def sum(a,b):
    return a+b

res = sum([1,2,3],[1,2,3])
print(res)

print (sum(1,2))