def f1(f):
    def f2():
        print('hello world!')
        f()
        print('Hello world')
    return f2

@f1
def f3():
    print('Bye World')

f3()