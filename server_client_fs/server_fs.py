import errno
import sys
import socket
from server_client_fs.constants import *

class Server:


    def __init__(self, msg):
        try:
            self.msg = msg

            # define the socket, and its options
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

            # declare empty list of connections made and peers
            self.connections = []
            self.peers = []

            # bind or attach the host IP and port to the socket
            self.s.bind((HOST, PORT))
            self.s.listen(1)

            print("-"*20 + "SOCKET SUCCESSFULLY CREATED" + "-"*20)
            print("-"*20 + "SERVER RUNNING" + "-"*20)
            self.run()
        except Exception as e:
            print("! " + "SOCKET CREATION FAILED" + " !")
            print("! " + "%s" %(errno) + " !")
            sys.exit()
            pass


    def handler(self, connection, a):
        try:
            while True:
                # the peer acting as the server recieves the message
                data = connection.recv(BYTE_SIZE)
                for connection in self.connections:
                    # the current peer that is connected wants to quit
                    if data and data.decode("utf-8")[0].lower() == 'q':
                        # disconnects the peer
                        self.disconnect(connection, a)
                        return

                    elif data and data.decode("utf-8") == REQUEST_STRING:
                        print("-"*20 + "UPLOADING" + "-"*20)
                        # send back any data if the connection is still active
                        # below is the uploading of the file
                        connection.send(self.msg)
        except Exception as e:
            sys.exit()


    def disconnect(self, connection, a):
        self.connections.remove(connection)
        self.peers.remove(a)
        
        connection.close()
        self.send_peers()

        print(f"{a}, disconnected")
        print("-"*20)


    def run(self):
        # constantly listen for available connections
        while True:
            # accept connections and append peers to the list
            connection, a = self.s.accept()
            self.peers.append(a)
            print(f"Peers are: {self.peers}")
            self.send_peers()

            # create thread for one connection
            c_thread = threading.Thread(target=self.handler, args=(connection,a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print(f"{a}, connected")
            print("-"*20)

    def send_peers(self):
        peer_list = ""

        for peer in self.peers:
            peer_list = peer_list + str(peer[0] + ", ")

        for connection in self.connections:
            # use the byte value of 11 at the beginningof a byte
            # in order differentiate from  whether one message from another
            data = PEER_BYTE_DIFF + bytes(peer_list,"utf-8")
            connection.send(PEER_BYTE_DIFF + bytes(peer_list,"utf-8"))