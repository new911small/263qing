import urllib2
import filecmp
print filecmp.cmp('./first.py', './second.py')
a = 'D:\dir2'
b = 'D:\dir1'
dirobj=filecmp.dircmp(a,b,['text.txt'])
dirobj.report()

dirobj.report_full_closure()
dirobj.report_partial_closure()
print 'zuomulu'+str(dirobj.left_list)
print 'common:'+str(dirobj.common)
print 'common files:'+str(dirobj.common_files)
print 'common dir:'+str(dirobj.common_dirs)

print 'mmmssss----------------------mmmssss'
