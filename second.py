import psutil,datetime
mee = psutil.virtual_memory()
print mee.total, mee.used
print psutil.cpu_times()
print psutil.cpu_times(percpu=True)
print psutil.cpu_times().system
print psutil.cpu_times().user
print '-------------------------------------'
print psutil.cpu_count()
print psutil.virtual_memory().used
print psutil.swap_memory()
print 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
print psutil.disk_io_counters()
print psutil.net_io_counters()
print psutil.net_io_counters(pernic=True)
print psutil.users()
print psutil.boot_time()
m=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print m
