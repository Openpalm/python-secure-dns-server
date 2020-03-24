from envparse import env
import socket
import ssl


class Props:

    RESOLVER_HOSTNAME = env('RESOLVER_HOSTNAME', "cloudflare-dns.com")
    RESOLVER_IP = env('RESOLVER_IP', "1.1.1.1")
    RESOLVER_PORT = int(env('RESOLVER_PORT', 853))

    APP_BIND_HOST = env('APP_BIND_HOST', "0.0.0.0")
    APP_BIND_PORT = int(env('APP_BIND_PORT', 53))

    THREAD_TIMEOUT = 1


class DnsRequest:

    def resolve(query):
        print(query)
        server = (Props.RESOLVER_IP, Props.RESOLVER_PORT)
        cx = ssl.create_default_context()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            with cx.wrap_socket(sock, server_hostname=Props.RESOLVER_HOSTNAME) as ssock:
                ssock.connect(server)
                ssock.send(query)
                data = ssock.recv(1024)
                return data
