from client0 import Client

FOLDER = "../Session-04/"
PRACTICE = 3
EXERCISE = 7
SEQUENCE = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT = 8080
c = Client(IP, PORT)

ping = c.talk("PING")
print(f"* Testing PING...\n {ping}")

get0 = c.talk("GET 0")
get1 = c.talk("GET 1")
get2 = c.talk("GET 2")
get3 = c.talk("GET 3")
get4 = c.talk("GET 4")
print(f"* Testing GET...\nGET 0: {get0}\nGET 1: {get1}\nGET 2: {get2}\nGET 3: {get3}\nGET 4: {get4}\n")

info = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"* Testing INFO...\n{info}\n")

comp = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"* Testing COMP...\nCOMP {SEQUENCE}\n{comp}")

rev = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"* Testing REV...\nREV {SEQUENCE}\n{rev}")

gene_u5 = c.talk("GENE U5")
gene_ada = c.talk("GENE ADA")
gene_frat1 = c.talk("GENE FRAT1")
gene_fxn = c.talk("GENE FXN")
gene_rnu6 = c.talk("GENE RNU6_269P")
print(f"* Testing GENE...\nGENE U5\n{gene_u5}\nGENE ADA\n{gene_ada}\n\nGENE FRAT1\n{gene_frat1}\n\nGENE FXN\n{gene_fxn}\n\nGENE RNU6_269P\n{gene_rnu6}")
