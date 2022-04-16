import http.server
import socketserver
import termcolor
import pathlib
from class_seq import Seq

PORT = 8085
FOLDER = "../Session-04/"

def get(msg):
    seq_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
                "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
                "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
                "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
                "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
    seq = seq_list[int(msg)]
    return seq

def gene(msg):
    gene_file = FOLDER + msg + ".txt"
    s = open(gene_file, "r").read()
    s = s[s.find("\n"):]
    return s

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

def info(s):
    dict = bases_percentage(s)
    response = "Total length: " + str(s.len()) + "\n"
    response += info_message(dict)
    return response


socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        print("PATH:", self.path)
        services_list = ["get", "gene", "operation"]
        if self.path == "/" or self.path == "/favicon.ico":
            contents = pathlib.Path("html/index.html").read_text()
        else:
            try:
                split_path = self.path.split("?")
                filename = split_path[0].replace("/", "")
                if filename in services_list:
                    msg = split_path[1].split("=")[1]
                if filename == "get":
                    seq = get(msg)
                    contents = pathlib.Path("html/" + filename + ".html").read_text().format(num=msg, seq=seq)
                elif filename == "gene":
                    s = gene(msg)
                    contents = pathlib.Path("html/" + filename + ".html").read_text().format(gene_name=msg, gene=s)
                elif filename == "operation":
                    operation_type = split_path[1].split("=")[2]
                    msg = msg.split("&")[0]
                    s = Seq(msg)
                    if s.valid_sequence():
                        if operation_type == "info":
                            result = info(s)
                        elif operation_type == "comp":
                            result = s.complement()
                        else:
                            result = s.reverse()
                        contents = pathlib.Path("html/" + filename + ".html").read_text().format(seq=msg,
                                                                                                 operation_type=operation_type,
                                                                                                 result=result)
                    else:
                        contents = pathlib.Path("html/error.html").read_text()
                else:
                    contents = pathlib.Path("html/" + filename + ".html").read_text()
            except FileNotFoundError:
                contents = pathlib.Path("html/error.html").read_text()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return

Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()