import paramiko

ssh = paramiko.SSHClient()
policy = paramiko.AutoAddPolicy
ssh.set_missing_host_key_policy(policy)
ssh.connect(
    hostname='192.168.1.22',
    port=22,
    username='root',
    password = '123456'
)
sftp_client = ssh.open_sftp()
remote_file=sftp_client.open('/opt/backsvr/logs/result.txt')
# stdin,stdout,stderr = ssh.exec_command('cd /opt/backsvr/logs')
# f=open('./result.txt','r')
# kk=f.readlines()
for i in remote_file:
    re
    l='/gensee/platform/bin/ucflash2hlstool '+i+'0 10 1 1'
    print l
    stdin,stdout,stderr = ssh.exec_command(l)

print 'jieshu'
remote_file.close()
