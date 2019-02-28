
print '----------------------------------'
b=['jsg',11,'ksfh',667,'kfj']
print len(b)

t1=('aaa','bbb','cccc')
print t1[:2]

name='hanhuaxx'
if name=='liubiqing':
    print'haha,tahaocomngminga'
elif name=='hanhuanfei':
    print 'hehe,zuibenle'
else:
    print 'kaixinjiuhaoya'


i=3
while i < 10:
    print i
    i = i + 1

for i in range(7):
    if i==3:
        break
    print i

def kaka():
    print 'abcdefghijk'
kaka()
print '************************************************'

a = 1
def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
print a

b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print change_list(b)
print b



