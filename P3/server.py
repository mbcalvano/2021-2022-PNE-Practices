import socket
from termcolor import colored
from seq1 import Seq

seq_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
            "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
            "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
            "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
            "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]


def bases_percentage(s):
    d = s.count()
    total = sum(d.values())
    for k, v in d.items():
        d[k] = [v, round((v * 100) / total, 1)]
    return d


def info_message(dict):
    message = ""
    for k, v in dict.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)\n"
    return message


def info(arg, s):
    dict = bases_percentage(s)
    response = "Sequence: " + arg + "\n"
    response += "Total length: " + str(s.len()) + "\n"
    response += info_message(dict)
    return response


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"
FOLDER = "../Session-04/"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server configured!")

while True:
    print("Waiting for clients...")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        allowed_cmd = ["PING", "GET", "INFO", "REV", "COMP", "GENE"]
        if cmd in allowed_cmd:
            print(colored(cmd, "green"))
            if cmd != "PING":
                arg = splitted_command[1]
            if cmd == "PING":
                response = "OK!\n"
            elif cmd == "GET":
                try:
                    index = int(arg)
                    response = seq_list[index]
                except ValueError:
                    response = "The argument should be a number between 0 and 4"
                except IndexError:
                    response = "The argument should be a number between 0 and 4"
            elif cmd == "INFO":
                s = Seq(arg)
                if s.valid_sequence():
                    response = info(arg, s)
                else:
                    response = "Please enter a valid DNA sequence"
            elif cmd == "COMP":
                s = Seq(arg)
                response = s.complement() + "\n"
            elif cmd == "REV":
                s = Seq(arg)
                response = s.reverse() + "\n"
            elif cmd == "GENE":
                s = Seq()
                s.read_fasta(FOLDER + arg + ".txt")
                response = f"{s}\n"
        else:
            response = "This command is not available in the server\n"
        print(response)
        cs.send(response.encode())
        cs.close()
