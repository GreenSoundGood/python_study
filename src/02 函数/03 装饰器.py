def welcome(fn):
    def a(*args, **kwargs):
        print('welcome')
        result = fn(*args, **kwargs)
        return result
    return a

@welcome
def fanc1(messger:str):
    print(f"hello, {messger}")

@welcome
def fanc2():
    print('This is fanc2')

fanc1('CODM')
fanc2()