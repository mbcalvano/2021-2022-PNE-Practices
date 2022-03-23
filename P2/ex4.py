from client0 import Client
from seq1 import Seq
from termcolor import colored

FOLDER = "../Session-04/"
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

s1 = Seq()
s1.read_fasta(FOLDER + "FRAT1.txt")
s2 = Seq()
s2.read_fasta(FOLDER + "ADA.txt")
s3 = Seq()
s3.read_fasta(FOLDER + "FXN.txt")

sequences = [s1, s2, s3]
genes = ["FRAT1", "ADA", "FXN"]

i = 0

for s in sequences:
    print("To server: " + colored("Sending " + genes[i] + " gene to the server...", "blue"))
    response = c.talk("Sending " + genes[i] + " gene to the server...")
    print(f"From server:\n\n{response}\n\n")
    print("To server: " + colored(str(s), "blue"))
    response2 = c.talk(str(s)) #LE DA COLOR AL RESTO DE LAS LINEAS
    print(f"From server:\n\n{response2}\n\n")
    i += 1
