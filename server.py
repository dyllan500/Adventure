import socket
import threading

class Server:
    connections = []
    peers = {
        "p1":"",
        "p2":""
    }
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5051))
    s.listen(3)

    def handler(self, c, addr):
        while True:
            data = c.recv(1024).decode("utf-8")
            for d in data:
                for i in "|":
                    if d == "|":
                        split = data.split("|")
                        user = split[0]
                        data = split[1]
                        for peer in self.peers:
                            if user != peer:
                                self.peers[peer].send((data).encode("utf-8"))
                                if not data:
                                    print(str(addr[0]) + ":" + str(addr[1]), "Dis-connected")
                                    self.connections.remove(c)
                                    c.close()
                                    break

    def run(self):
        while True:
            (c, addr) = self.s.accept()
            cThread = threading.Thread(target=self.handler, args=(c, addr))
            cThread.daemon = True

            if self.peers["p1"] == "":
                self.peers["p1"] = c
                for peer in self.peers:
                    if "p1" == peer:
                        self.peers[peer].send("p1".encode("utf-8"))
                print("sent")
            elif self.peers["p2"] == "":
                self.peers["p2"] = c
                for peer in self.peers:
                    if "p2" == peer:
                        self.peers[peer].send("p2".encode("utf-8"))
                print("sent2")
            else:
                self.connections.append(c)
            cThread.start()
            print(str(addr[0]) + ":" + str(addr[1]), "Connected")

def main():
    server = Server()
    server.run()
if __name__ == "__main__":
    main()