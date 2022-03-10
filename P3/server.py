import socket
from termcolor import colored
from seq1 import Seq

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
                seq_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
                if 0 <= int(arg) <= 4:
                    response = seq_list[int(arg)]
                else:
                    response = "The argument should be a number between 0 and 4"
            elif cmd == "INFO":
                s = Seq(arg)
                d = s.count()
                list_bases = ["A", "T", "C", "G"]
                percentage_a = round(d[list_bases[0]] * 100 / s.len(), 1)
                percentage_c = round(d[list_bases[2]] * 100 / s.len(), 1)
                percentage_g = round(d[list_bases[3]] * 100 / s.len(), 1)
                percentage_t = round(d[list_bases[1]] * 100 / s.len(), 1)
                response = f"Sequence: {arg}\nTotal length: {s.len()}\nA: {d[list_bases[0]]} ({percentage_a}%)\nC: {d[list_bases[2]]} ({percentage_c}%)\nG: {d[list_bases[3]]} ({percentage_g}%)\nT: {d[list_bases[1]]} ({percentage_t}%) "
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
