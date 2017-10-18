import socket
import select


class Server:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 2000))
        self.socket_list = [self.server]
        self.addresses = ['localhost']
        self.commands = [""]
        self.running = True
        self.server.listen(10)

    def listen(self):
        while self.running:
            read, write, error = select.select(self.socket_list, [], self.socket_list, 0)
            for sock in read:
                if sock == self.server and self.running:
                    try:
                        conn, address = self.server.accept()
                        conn.settimeout(10)
                        self.socket_list.append(conn)
                        self.addresses.append(address[0])
                        self.commands.append("")
                    except:
                        self.shutdown()
                        break
                elif self.running:
                    try:
                        packet = sock.recv(60)
                        print('packet received')
                        if not packet:
                            self.close_conn(sock)
                        index = self.socket_list.index(sock)
                        self.commands[index] += packet
                        if '\n' in self.commands[index]:
                            print('handle')
                    except:
                        self.close_conn(sock)

    def close_conn(self, conn):
        print('close client conn')

    def shutdown(self):
        print('shutdown server')


if __name__ == "__main__":
    Server().listen()