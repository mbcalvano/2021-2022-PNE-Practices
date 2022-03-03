from client0 import Client
from seq1 import Seq
from termcolor import colored

FOLDER = "../Session-04/"
PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

s = Seq()
s.read_fasta(FOLDER + "FRAT1.txt")
fragment1 = "Fragment 1: " + str(s)[:10]
fragment2 = "Fragment 2: " + str(s)[10:20]
fragment3 = "Fragment 3: " + str(s)[21:31]
fragment4 = "Fragment 4: " + str(s)[32:42]

print("Gene FRAT1:", str(s))
print(fragment1)
print(fragment2)
print(fragment3)
print(fragment4)


green_message = colored("Sending FRAT1 Gene to the server, in fragments of 10 bases...", "green")
c.talk(green_message)
c.talk(colored(fragment1, "green"))
c.talk(colored(fragment2, "green"))
c.talk(colored(fragment3, "green"))
c.talk(colored(fragment4, "green"))
