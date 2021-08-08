import sys

line1="[winhost]"
line2=str(sys.argv[1])
line3="[winhost:vars]"
line4="ansible_user="+sys.argv[2]
line5="ansible_password="+ sys.argv[3]
line6="ansible_connection=winrm \nansible_winrm_server_cert_validation=ignore"
file = open(r'hosts','w')
hostsdata= line1 +'\n'+ line2+'\n' + line3+'\n' + line4+'\n' + line5+'\n' + line6
file.write(hostsdata)
file.close()
file = open(r'hosts','r')
print(file.read())
