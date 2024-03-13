import socket
import threading

def readLine(sock):
    a = ''
    while True:
        msg = sock.recv(1)
        if (msg == b'\n'):
            break;
        a += msg.decode()
    return(a)

def worker(sock):
    try:
        while True:
            line = readLine(sock)
            print(line)
            message = line
            sock.sendall(message.encode())
            if line == "EXIT":
                print('ending connection')
                break
    finally:
        # Clean up the connection
        sock.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 10009)
sock.bind(server_address)

sock.listen(5)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)

    t = threading.Thread(target=worker, name='Daemon', args=(connection,))
    t.start()
