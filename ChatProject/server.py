__author__ = 'Fabian'

import socket


class RpChatServer():

    def __init__(self):

        self.host = ''
        self.port = 10244
        self.backlog = 5
        self.size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind((self.host, self.port))
        self.socket.listen(self.backlog)
        while 1:
            print('Running')
            client, address = self.socket.accept()
            data = client.recv(self.size).decode()
            if data:
                client.send(data.encode())
            client.close()


def main():
    server = RpChatServer()


if  __name__ =='__main__':
    main()