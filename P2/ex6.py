from client0 import Client
from seq1 import Seq
from termcolor import colored

FOLDER = "../Session-04/"
PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"

# -- Create a client object
c1 = Client(IP, 8080)
c2 = Client(IP, 8081)

s = Seq()
s.read_fasta(FOLDER + "FRAT1.txt")
fragment1 = "Fragment 1: " + str(s)[:10]
fragment2 = "Fragment 2: " + str(s)[10:20]
fragment3 = "Fragment 3: " + str(s)[21:31]
fragment4 = "Fragment 4: " + str(s)[32:42]
fragment5 = "Fragment 5: " + str(s)[43:53]
fragment6 = "Fragment 6: " + str(s)[54:64]
fragment7 = "Fragment 7: " + str(s)[65:75]
fragment8 = "Fragment 8: " + str(s)[76:86]
fragment9 = "Fragment 9: " + str(s)[87:97]
fragment10 = "Fragment 10: " + str(s)[98:108]

print("Gene FRAT1:", str(s))
fragment_list = [fragment1, fragment2, fragment3, fragment4, fragment5, fragment6, fragment7, fragment8, fragment9, fragment10]
for f in fragment_list:
    print(f)

green_message = colored("Sending FRAT1 Gene to the server, in fragments of 10 bases...", "green")
c1.talk(green_message)
c2.talk(green_message)
even_fragments = [fragment2, fragment4, fragment6, fragment8, fragment10]
odd_fragments = [fragment1, fragment3, fragment5, fragment7, fragment9]
for e in even_fragments:
    c2.talk(colored(e, "green"))
for o in odd_fragments:
    c1.talk(colored(o, "green"))