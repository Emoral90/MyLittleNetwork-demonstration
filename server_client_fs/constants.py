import socket
import threading
import sys
import time
from random import randint
# Find library that supports .iso or .exe files\
# import 

BYTE_SIZE = 1024
HOST = "127.0.0.1"
PORT = 12347
PEER_BYTE_DIFF = b"\x11"
RAND_TIME_START = 1
RAND_TIME_END = 2
REQUEST_STRING = "req"
