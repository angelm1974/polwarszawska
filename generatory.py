def gen_parzyste(N):
    for i in range(N):
        if i % 2 == 0:
            yield i

gen=gen_parzyste(10)
# print(list(gen))
next(gen)
next(gen)
print(next(gen))
# print(list(gen))