from server_client_fs.constants import *
from server_client_fs.client_fs import Client
from server_client_fs.server_fs import Server
from fileIO import *


# This class will take care of converting client to server
class p2p:
    # make ourself the default peer
    peers = ['127.0.0.1']


def main():
    # if the server breks we try to make a client a new server by setting msg = convert()
    msg = fileIO.convert_to_bytes()
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 -5 for immersion
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass

                # you become the server
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()
