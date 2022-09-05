def  old_f1(x):
    return x**2

def  old_f2(x):
    return x**3

def  old_f3(x):
    return x**4

# def old_f1_new(*args, **kwargs):
#     print('LOG-begin')
#     rez = old_f1(*args, **kwargs)
#     print('LOG-end')
#     return rez

def log_func(func):                     # \
    def new_func(*args, **kwargs):      #  \
        print('LOG-begin')              #   \
        rez = func(*args, **kwargs)     #    => декоратор
        print('LOG-end')                #   /
        return rez                      #  /
    return new_func                     # /

old_f1_new = log_func(old_f1) # новая функция = преобразователь (старой функции) (функциональный вид декоратора)
old_f2_new = log_func(old_f2)
old_f3_new = log_func(old_f3)

def log_func(func):                     # \
    def new_func(*args, **kwargs):      #  \
        print('LOG-begin')              #   \
        rez = func(*args, **kwargs)     #    => декоратор
        print('LOG-end')                #   /
        return rez                      #  /
    return new_func                     # /

def old_f1(x):
    return x**2
old_f1 = log_func(old_f1) # декорация напрямую (в лоб)

@log_func       # декорация - синтаксический "сахар"
def old_f2(x):
    return x**3

def old_f3(x): # без декорации
    return x**5
