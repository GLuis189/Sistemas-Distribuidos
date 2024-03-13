import socket
import sys

def writeLine(sock, string):
    sock.sendall(string.encode())
    sock.sendall(b'\n')
    data = sock.recv(1024)
    print(data.decode())

arguments = len(sys.argv)
if arguments < 3:
    print('Uso: client_calc  <host> <port>')
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (sys.argv[1], int(sys.argv[2]))
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    while(1):
        str = input(">>> ")
        if str == "EXIT":
            writeLine(sock, str)
            break
        writeLine(sock, str)
    
finally:
    print('closing socket')
    sock.close()
