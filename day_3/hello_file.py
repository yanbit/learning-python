# coding:utf-8

f = open('name.txt','w')
f.write('hello mv')
f.close()






f2 = open('name.txt','a')
f2.write('hello sg')
f2.close()

f1 = open('name.txt')
print(f1.read())
f1.close()