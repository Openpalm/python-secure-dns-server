import socketserver
import threading
import time
from utils import DnsRequest, Props

class TCPHandler(socketserver.BaseRequestHandler):
    """
    Handles the TCP Requests

    in: b'\x00=\xec!\x01 \x00\x01\x00\x00\x00\x00\x00\x01\x04news\x0bycombinator\x03com\x00\x00\x01\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x0c\x00\n\x00\x08\x91.\n\xb1DR\xb3\xf6'

    out: b'\x00A\xec!\x81\x80\x00\x01\x00\x01\x00\x00\x00\x01\x04news\x0bycombinator\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x008\x00\x04\xd1\xd8\xe6\xf0\x00\x00)\x05\xac\x00\x00\x00\x00\x00\x00'
    """
    def handle(self):
        self.data = self.request.recv(1024).strip()
        result = DnsRequest.resolve(self.data)
        print("{} Processing TCP request .. ".format(threading.current_thread()))
        print("TCP Request: {} ".format(self.data))
        print("TCP Reply: {} ".format(result))
        self.request.sendall(result)

class UDPHandler(socketserver.DatagramRequestHandler):
    """
    Handles the UDP Requests

    in:
        (b'\x99\xff\x01 \x00\x01\x00\x00\x00\x00\x00\x01\x06google\x03com\x00\x00\x01\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x0c\x00\n\x00\x08\xbfk\xef\xf4\x16\x11 \r',
        <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('0.0.0.0', 53)>)

    out:
        b'\x007\xbd\xcd\x81\x80\x00\x01\x00\x01\x00\x00\x00\x01\x06google\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00\x0e\x00\x04\xac\xd9\x17n\x00\x00)\x05\xac\x00\x00\x00\x00\x00\x00'
    """
    def handle(self):
        datagram = self.request[0]
        datagram = "\x00".encode() + chr(len(datagram)).encode() + datagram
        result = DnsRequest.resolve(datagram)
        print("{} Processing UDP request .. ".format(threading.current_thread()))
        print("UDP Request: {} ".format(self.request))
        print("UDP Reply: {} ".format(result))
        self.wfile.write(result[2:])


if __name__ == "__main__":
    """
    Listens on port 53/udp/tcp for DNS requests
    Sends requests over TLS to 1.1.1.1 / cloudflare-dns.com
    """

    print("app started at {} {}\n".format(
        Props.APP_BIND_HOST,
        Props.APP_BIND_PORT))

    def run():
        serverInfo = (Props.APP_BIND_HOST, Props.APP_BIND_PORT)
        servers = []

        servers.append(socketserver.ThreadingTCPServer(serverInfo, TCPHandler, True))
        servers.append(socketserver.ThreadingUDPServer(serverInfo, UDPHandler, True))

        for server in servers:
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            server_thread.join(Props.THREAD_TIMEOUT)

        # Keep main thread alive
        while (True):
            threading.Event().wait(1)
   # App Start
run()
