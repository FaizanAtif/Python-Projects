def gen():
    i = 1
    while i < 10:
        yield i
        i += 1

gen_num = gen()

print(next(gen_num))
print(next(gen_num))
print(next(gen_num))
