import socket
from threading import Thread
import struct
import json
import time
from threading import Lock

MCAST_ADDR = ('225.0.0.250', 5007)
TCP_IP = '127.0.0.1'
MCAST_PORT = 6789

# multicast_group = '225.0.0.250'
# server_address = ('', 10000)


class IntelligentObj:

    id_increment = 0


    def __init__(self, type, obj):
        self.type = type
        self.mcast_sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_sock.bind((TCP_IP, 0))
        self.connected = False
        self.lock = Lock()
        self.obj = obj
        self.obj.id = self.get_id()
        self.tr = Thread(target=self.wait_for_call, args=())
        self.tr.start()

    def notify_presence(self, ip, port):
        print("entrou no notify presence - ", self.type)
        TCP_PORT = self.tcp_sock.getsockname()[1]
        id = {"type": self.type, "ip": TCP_IP, "port": TCP_PORT}

        if not self.connected:
            self.tcp_sock.connect((ip, port))
            self.tcp_sock.sendall(bytes(json.dumps(id), "utf-8"))
            self.connected = True

        time.sleep(0.5)
        self.send_status()
        

    def wait_for_call(self):

        self.mcast_sock.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("--->>>PRINTANDO ADDR: ", MCAST_ADDR)
        self.mcast_sock.bind(MCAST_ADDR)

        mreq = struct.pack('4sl', socket.inet_aton(
            MCAST_ADDR[0]), socket.INADDR_ANY)
        self.mcast_sock.setsockopt(
            socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        
        print("Waiting: ", self.type)
        data = self.mcast_sock.recv(10240)
        cmd = json.loads(data.decode('utf-8'))
        print(cmd)
        self.notify_presence(cmd["ip"], cmd["port"])
        #time.sleep(0.5)
        #self.send_status()
        
    def get_id(self):
        IntelligentObj.id_increment += 1
        return str(IntelligentObj.id_increment)
    def send_status(self):
        #self.tr.join()
        if self.connected:
            print("sending status ", self.type)
            self.tcp_sock.sendall(self.obj.SerializeToString())
            print("Enviado ", self.type)