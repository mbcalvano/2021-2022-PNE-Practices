from client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.73"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)