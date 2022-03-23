import socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()
    print("A client has connected to the server")
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    print(f"Message received: {msg}")
    response = "HELLO. I am the Happy Server :-)\n"
    cs.send(response.encode())
    cs.close()
