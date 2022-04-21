import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from class_seq import Seq

HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["ACGTCCAGTAAA", "ACGTAGTTTTTAAACCC", "GGGTAAACTACG",
                  "CGTAGTACGTA", "TGCATGCCGAT", "ATATATATATATATATATA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU5A", "U5"]
FOLDER = "../Session-04/"
PORT = 8085

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents



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
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)
        if self.path == "/" or self.path == "/favicon.ico":
            contents = read_html_file("index.html")\
                .render(context=
                        {"n_sequences": len(LIST_SEQUENCES),
                         "genes": LIST_GENES})
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence
            })
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = Path(FOLDER + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html") \
                .render(context={
                "gene_name": gene_name,
                "sequence": sequence
            })
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            s = Seq(sequence)
            if s.valid_sequence():
                if operation == "info":
                    contents = read_html_file(path[1:] + ".html") \
                        .render(context={
                        "sequence": sequence,
                        "operation": operation,
                        "result": info(s)
                    })
                elif operation == "comp":
                    contents = read_html_file(path[1:] + ".html") \
                        .render(context={
                        "sequence": sequence,
                        "operation": operation,
                        "result": s.complement()
                    })
                else:
                    contents = read_html_file(path[1:] + ".html") \
                        .render(context={
                        "sequence": sequence,
                        "operation": operation,
                        "result": s.reverse()
                    })
            else:
                contents = Path("html/error.html").read_text()
        else:
            try:
                contents = Path(HTML_FOLDER + path + ".html").read_text()
            except FileNotFoundError:
                contents = Path("html/error.html").read_text()


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
        print("Stopped by the user")
        httpd.server_close()
