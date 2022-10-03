import time
import request_pb2
from threading import Timer
from intelligent_obj import IntelligentObj

from threading import Thread

MCAST_GRP = TCP_IP = 'localhost'
MCAST_PORT = 6789


class Treadmill(IntelligentObj):
    def __init__(self):
        treadmill = request_pb2.Treadmill()
        treadmill.type = "Treadmill"
        treadmill.dist = 0.0
        treadmill.vel = 0.0
        super().__init__("treadmill", treadmill)
        self.increase_dist()
        commands_map = {"turn_on": self.turn_on,"turn_off": self.turn_off,"increase_vel": self.increase_vel,"decrease_vel": self.decrease_vel}
        self.fill_cmd_list(commands_map.keys())
        Thread(target=self.wait_for_command, args=(commands_map,)).start()

    def turn_on(self):
        self.obj.status = True
        self.send_status()

    def turn_off(self):
        self.obj.status = False
        self.vel = 0.0
        self.dist = 0.0
        self.send_status()

    def increase_vel(self):
        if self.obj.status == True:
            self.obj.vel += 5
            self.obj.vel = 40.0 if self.obj.vel > 40.0 else self.obj.vel
            self.send_status()

    def increase_dist(self):
        Timer(5.0, self.increase_dist, args=()).start()
        with self.lock:
            if self.obj.vel > 0:
                self.obj.dist += 10.0

        self.send_status()

    def decrease_vel(self):
        if self.obj.status == True:
            self.obj.vel -= 5
            self.obj.vel = 0.0 if self.obj.vel < 0.0 else self.obj.vel
            self.send_status()

    def to_str(self):
        print(self.obj.status)
        print(self.obj.type)
        print(self.obj.dist)
        print(self.obj.vel)

    # def notify_presence(self, ip, port):
    #     super().notify_presence(ip, port)
    #     time.sleep(0.5)
    #     self.send_status()

    # def send_status(self):
    #     Timer(5.0, self.send_status, args=()).start()
    #     super().send_status()

        

    



    

    # def send_object(self):

    #     data = self.tcp_sock.recv(10240)
    #     cmd = json.loads(data.decode('utf-8'))