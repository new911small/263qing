import httplib
import dns.resolver
coon = httplib.HTTPConnection('www.baidu.com')
coon.request('GET','/')
r=coon.getresponse()
print r.read(15)
print r.status
print "======++++++++!!!!!!!"
a = dns.resolver.query('www.baidu.com','A')
print a
print a.response.answer
for i in a.response.answer:
    print i
    for j in i.items:
        print j
