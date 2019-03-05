# coding:utf-8

f = open('name.txt')
data = f.read()
print(data.split('|'))

f2= open('weapon.txt')
# data = f2.read()

i=1
for line in f2.readlines():
    if i%2 ==1 :
        print(line.strip())
    i+=1