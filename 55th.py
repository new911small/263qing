from functools import reduce

def jia(x,y):
    if y > 9:
        return x+y
c = map(jia,[4,5,6,13,15],[1,2,13,14,15])

aa = list(c)
print aa

def f(x):
    x[0] = 100
    print x

a = [1,2,3]
f(a)
print a

print cmp(2.3, 3.2)

dict1=dict(a=1,b="hello",c=[1,2,3])
print dict1

f=dict1.get('a')
print f

exec("print('Hello')")
eval(compile("print('Hello')",'test.py','exec')  )
class Jia(object):
    def yaya(self):
        print 'hahahahaha'
n=Jia()
m=repr(n)
print m

# compile("print('Hello')")

ff=dict(a=20,b='kkkk',c='ff')
print ff

kgm='adjsd'+'12ksfj'
print kgm




