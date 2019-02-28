

class bird(object):
    egg='two'
    yumao='yaya'
    def move(self):
        print 'hhhaa %s'%(self.egg)
summer=bird()
summer.move()

class Newyear(object):
    def __init__(self,a):
        self.name=a
bb=Newyear('qingzi')
# print Newyear.name

print dir(list)

f1=['yaya','kan',111,678]
f2=f1.pop()
print f2

class yyy(list):
    def __sub__(self, other):
        a=self[:]
        b=other[:]
        while len(b)>0:
            m=b.pop()
            if m in a:
                a.remove(m)
        return a

print yyy([3,4,5])-yyy([3,4,8])

dir1={1:[11,22,33],"aa":['biqing','111']}
print dir1

dir2={'name':'liubiqing','age':26,'sam':"qiqi"}
for a in dir2:
    print dir2[a]

del dir2['name']
print dir2

f=open('./diff.html','r')
# print f.read()
print '+++++++++++++++++++++++'
for i in xrange(5):
    print f.readline()
print 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
# print f.readlines()

def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3)

print '************************'
def func(**dict):
    print type(dict)
    print dict

func(a=1,b=9)
func(m=2,n=1,c=11)

print '============================='
for i in range(1,10,2):
    print i

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
S='jsfjdhgfjhjd'
for index,m in enumerate(S):
    print index,m

print '++++++++++++++++'
m={'aa','bb','cc'}
d={11,22,33}
print dict(zip(m,d))

print '^^^^^^^^^^^^^^^^^^^^^^^^^'
f = open('./diff.html','r')

for i in range(10):
    print f.next()


def gen():
    a=2
    yield a
    b=3
    yield 3
    yield 1000

for i in xrange(2):
    c = gen()
    print c
print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
for i in gen():
    print i

c=(a**2 for a in range(4))
for i in c:
    print i
