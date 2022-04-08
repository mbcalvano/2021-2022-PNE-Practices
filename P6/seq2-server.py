import http.server
import socketserver
import termcolor
import pathlib

PORT = 8085

socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        print("PATH:", self.path)
        services_list = ["get", "gene"]
        if self.path == "/" or self.path == "/favicon.ico":
            contents = pathlib.Path("html/index.html").read_text()
        else:
            try:
                split_path = self.path.split("?")
                print(split_path)
                filename = split_path[0].replace("/", "")
                if filename in services_list:
                    option = split_path[1].split("=")[1]
                    contents = pathlib.Path("html/" + filename + "-" + str(option) + ".html").read_text()
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