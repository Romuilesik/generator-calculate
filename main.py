def gen(number, max_degree):
    num = 0
    for _ in range(max_degree):
        yield number**num
        num += 1

res = gen(2, 200)
print(res)
for num in res:
    print(num)