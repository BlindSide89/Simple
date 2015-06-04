__author__ = 'Fabian'

import socket

class RpChatClient():

    def __init__(self):

        self.host = 'localhost'
        self.port = 10244
        self.size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((self.host, self.port))
        self.socket.send('Hello World'.encode())
        data = self.socket.recv(self.size)
        self.socket.close()
        print('Received: ' + data.decode())


def main():
    client = RpChatClient()


if  __name__ =='__main__':
    main()