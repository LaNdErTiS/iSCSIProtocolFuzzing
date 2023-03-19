import socket
import threading

from random import randbytes
from random import randint

# Variables for holding information about connections
connections = []
total_connections = 0


# Client class, new instance created for each connected client
# Each instance has the socket and address that is associated with items
# Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server and send it back to every
    # client aside from the client that has sent it
    # .decode is used to convert the byte data into a printable string
    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(330)
            except:
                print("Client " + str(self.address[1]) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if data != "":
                print("ID " + str(self.id) + ": " + str(data))
                for client in connections:
                    if len(data) == 312:
                        index = 0 #randint(1, 100)
                        sr = b'\x23\x87\x00\x00\x00\x00\x00\x8e\x00\x02\x3d\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00' \
                            b'\x00\x00\x00\x00\x00\x00\x54\x61\x72\x67\x65\x74\x50\x6f\x72\x74\x61\x6c\x47\x72\x6f' \
                            b'\x75\x70\x54\x61\x67\x3d\x31\x00\x48\x65\x61\x64\x65\x72\x44\x69\x67\x65\x73\x74\x3d\x4e' \
                            b'\x6f\x6e\x65\x00\x44\x61\x74\x61\x44\x69\x67\x65\x73\x74\x3d\x4e\x6f\x6e\x65\x00\x44\x65' \
                            b'\x66\x61\x75\x6c\x74\x54\x69\x6d\x65\x32\x57\x61\x69\x74\x3d\x32\x00\x44\x65\x66\x61\x75' \
                            b'\x6c\x74\x54\x69\x6d\x65\x32\x52\x65\x74\x61\x69\x6e\x3d\x30\x00\x49\x46\x4d\x61\x72\x6b' \
                            b'\x65\x72\x3d\x4e\x6f\x00\x4f\x46\x4d\x61\x72\x6b\x65\x72\x3d\x4e\x6f\x00\x45\x72\x72\x6f' \
                            b'\x72\x52\x65\x63\x6f\x76\x65\x72\x79\x4c\x65\x76\x65\x6c\x3d\x30\x00\x00\x00'
                        sr = sr[:index] + randbytes(1) + sr[index + 1:]
                        client.socket.sendall(sr)
                    elif len(data) == 48:
                        client.socket.sendall(b'\x24\x80\x00\x00\x00\x00\x00\x58\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                                              b'\x01\xff\xff\xff\xff\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00'
                                              b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x54\x61\x72\x67\x65\x74\x4e\x61\x6d\x65\x3d'
                                              b'\x69\x71\x6e\x2e\x32\x30\x32\x33\x2d\x30\x32\x2e\x6c\x6f\x63\x61\x6c\x2e\x6f\x70'
                                              b'\x65\x6e\x6d\x65\x64\x69\x61\x76\x61\x75\x6c\x74\x3a\x74\x65\x73\x74\x2d\x6e\x61\x73'
                                              b'\x00\x54\x61\x72\x67\x65\x74\x41\x64\x64\x72\x65\x73\x73\x3d\x31\x39\x32\x2e\x31\x36\x38\x2e'
                                              b'\x30\x2e\x32\x33\x31\x3a\x33\x32\x36\x30\x2c\x31\x00')


# Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1


def main():
    # Get host and port
    host = '192.168.0.175' #input("Host: ")
    port = 3260 #int(input("Port: "))

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    # Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    newConnectionsThread.start()


main()
