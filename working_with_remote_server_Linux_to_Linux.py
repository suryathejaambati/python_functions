import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.83.139.48',username='ec2-user',key_filename='/home/ec2-user/.ssh/id_rsa',port=22)
stdin, stdout, stderr = ssh.exec_command('free -m')
print("The output is: ")
print(stdout.readlines())
print("The Error is: ")
print(stderr.readlines())

