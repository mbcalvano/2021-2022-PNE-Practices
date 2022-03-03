import socket
from termcolor import colored

# Configure the Server's IP and PORT
PORT = 8081
IP = "localhost" #MY IP address or "localhost" or 127.0.0.1 (=localhost)
#if we leave IP empty ("") -> works if using localhost
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating an object in the socket class
#there are many types of sockets, here we are defining that the type we are creating is af_inet
#STEPS -> create sock, bind to port, execute listen, execute accept
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS) #able to proceess in parallel up to 5 external clients

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept() #here it stops and waits for a client to connect, once that happens then it continues
        #with accept I get a socket to communicate with my client, through which I can either read or send information

        # Another connection!e
        number_con += 1 #increases for each connected client

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8") #2048 is a buffer where i'll store the client's information
        print("Message from client: {}".format(msg))

        # Send the messag
        message = colored("Hello from the teacher's server", "green")
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes) #prepared to receive an argument in bytes, not strings
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()