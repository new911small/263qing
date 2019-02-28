import difflib
test1 = '''my name is liubiqing I am working in 263 three days I must work hard and study much I 
       know everything is difficult when you start it  against myself 
       i want good better best
       i must study a lot
       fighting'''
f1=test1.splitlines()
# print f1
test2 = '''my name is liubiqing I am working in 263 three days I must work hard and study much I 
       know everything is difficult when you start it  against myself 
       i want good better best
       i must study 
       fighteeg'''
f2 = test2.splitlines()
d = difflib.Differ()
m = d.compare(f1, f2)
# print list(m)
print "\n".join(list(m))
print '@@@@@@-----------@@@@@@'
#列表里面必须是字符串
list1 = ['a', 'bbb', 'cd', 'fg', 'ah', 'jigf']
print '\n'.join(list1)