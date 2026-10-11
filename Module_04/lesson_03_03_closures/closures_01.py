def outer(par):
    loc = par
    return loc


var = 1
print(outer(var))


# print(par)
# print(loc)

def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var1 = 2
result = outer(var1)
print(result)
print(result())
