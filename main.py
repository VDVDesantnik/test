# def f():
#     return 10
#
# print(f)
# s = f
# print(s)
# print(s())

# s = print
# print(s)

# res = int
# r = res('10')
# print(r, type(r))
# s = list
# print(s('123456789'))

# def say_name():
#     def say_goodbye(name):
#         return f'hello {name}'
#     return say_goodbye
#
# f = say_name()
# print(f('Demian'))

# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#     return step
#
# def counter_add():
#     def step(start=0):
#         start += 5
#         return start
#     return step
#
# def f():
#     def f1(s):
#         return f'<h1>{s}</h1>'
#     return f1
#
# res = f()
# print(res('Python'))


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('-----------------------------')
        res = func(*args, **kwargs)
        print('-----------------------------')
        return res
    return wrapper


@func_decorator
def f(a, b):
    print(f'функция f {a} {b}')
    return 100

@func_decorator
def f1():
    return 10


print(f(10, 20))
print('--------------')
print(f1())

# def f(*args, **kwargs):
#     print(args)
#
# f(1,2,4,6,7,8,9,3,2,3,4,5)
