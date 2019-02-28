import difflib
test1 = '''hello my name is liubiqing
           from donbei
           i must study hard
           work hard
           study much'''

test2 = '''my name is hanhuanfei
           from henan
           mu qian zuode gongzuo shi pachong
           i must study much'''

list1 = test1.splitlines()
list2 = test2.splitlines()
d = difflib.HtmlDiff()
k = open('./diff.html','w')
print d.make_file(list1, list2)
k.write(d.make_file(list1, list2))
k.close()




