from client_class import Client
IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

message = c.talk("Hello")
print(message)