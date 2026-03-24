def Generator():
    yield "Round 1"
    yield "Round 2"
    yield "Round 3"

g=Generator()
print(next(g))

print(next(g))

print(next(g))

#or

def cube(n):
    for i in range(n):
        yield i * i


g=cube(5)

print(next(g))

print(next(g))


print(next(g))


print(next(g))


print(next(g))




