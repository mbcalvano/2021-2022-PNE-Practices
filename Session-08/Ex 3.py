import socket
#Everytime a new client connects to the server, it is allocated a new port
# SERVER IP, PORT
PORT = 8000
IP = "localhost"

while True:
  # -- Ask the user for the message
  msg = input("Introduce your message: ")

  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # -- Establish the connection to the Server
    s.connect((IP,PORT)) #This is a tuple, thats why we need two parenthesis, we only have to give one argument (the tuple)

  # -- Send the user message
    s.send(str.encode(msg))

  # -- Close the socket
    s.close()