import socket
import threading

class Server:
    connections = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5052))
    s.listen(3)

    def handler(self, c, addr):
        while True:
            data = c.recv(6400)
            if not data:
                print(str(addr[0]) + ":" + str(addr[1]), "Dis-connected")
                self.connections.remove(c)
                c.close()
                break
            sThread = threading.Thread(target=self.send, args=(data, c,))
            sThread.daemon = True
            sThread.start()


    def send(self, data, c):
        for peer in self.connections:
            if c != peer:
                peer.send(data)

    def run(self):
        while True:
            (c, addr) = self.s.accept()
            cThread = threading.Thread(target=self.handler, args=(c, addr,))
            cThread.daemon = True
            self.connections.append(c)
            cThread.start()
            print(str(addr[0]) + ":" + str(addr[1]), "Connected")

def main():
    server = Server()
    server.run()
if __name__ == "__main__":
    main()