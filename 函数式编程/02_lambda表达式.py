
f = lambda a,b,c:a+b+c

print(f)
print(id(f))
print(type(f))

print(f(10,20,30))

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(g[0](6),g[1](7),g[2](8))
