# -*- coding: utf-8
import socket
import threading
import time
from PyQt5.QtCore import pyqtSignal, QThread


class GetRawMsgThread(QThread):
    data_add_signal = pyqtSignal(str)
    
    def __init__(self):
        super(GetRawMsgThread, self).__init__()
        self.tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connTCP(self):
        # IP 和端口
        server_ip = 'bemfa.com'
        server_port = 8344
        try:
            # 连接服务器
            self.tcp_client_socket.connect((server_ip, server_port))
            # 发送订阅指令
            substr = 'cmd=1&uid=97c541e615ab43918f0a1e1a64d400ed&topic=Rocket\r\n'
            self.tcp_client_socket.send(substr.encode("utf-8"))
        except:
            time.sleep(2)
            self.connTCP()

    # 心跳
    def Ping(self):
        # 发送心跳
        try:
            keeplive = 'ping\r\n'
            self.tcp_client_socket.send(keeplive.encode("utf-8"))
        except:
            time.sleep(2)
            self.connTCP()
        # 开启定时，30秒发送一次心跳
        t = threading.Timer(30, self.Ping)
        t.start()

    def run(self):
        self.connTCP()
        self.Ping()

        while True:
            # 接收服务器发送过来的数据
            recvData = self.tcp_client_socket.recv(1024)
            if len(recvData) != 0:
                try:
                    self.data_add_signal.emit(recvData.decode('utf-8'))
                except UnicodeError:
                    pass
            else:
                self.data_add_signal.emit("cmd=-1")
                self.connTCP()
