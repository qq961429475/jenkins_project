def y_sample():
    for i in range(5):
        yield i
        print("yield i")
    yield 'end'


a = y_sample()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
