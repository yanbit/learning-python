alist = []
for i in range(1, 11):
    if i % 2 == 0:
        alist.append(i * i)
print(alist)

blist = [i * i for i in range(1, 11) if i % 2 == 0]
print(blist)

adict = {}
num = {i: 0 for i in {'x': 0, 'y': 1}}

print(num)
