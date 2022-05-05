import http.server
import socketserver
import termcolor
from urllib.parse import parse_qs, urlparse
import functions as f
import pathlib

PORT = 8080
FOLDER = "html/"
SERVER = "rest.ensembl.org"
ARGUMENT = "?content-type=application/json"


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", path)
        print("arguments", arguments)
        if path == "/":
            contents = pathlib.Path("html/index.html").read_text()
        elif path == "/listSpecies":
            try:
                dict_ensembl = f.ensembl("/info/species")
                list_species = []
                try:
                    n_species = int(arguments["limit"][0])
                except KeyError:
                    n_species = len([ele for ele in dict_ensembl["species"] if isinstance(ele, dict)])
                for i in range(n_species):
                    list_species.append(dict_ensembl["species"][i]["display_name"])
                print(n_species)
                if list_species[0] != "":  #QUÉ PASA SI EL LIMIT ES 0
                    contents = f.read_html_file("listSpecies.html") \
                        .render(context={
                        "n_species": n_species,
                        "list_species": list_species
                    })
                else:
                    contents = pathlib.Path("html/error.html").read_text()
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
            except IndexError:
                contents = pathlib.Path("html/error.html").read_text()
        elif path == "/karyotype":
            try:
                specie = arguments["specie"][0]
                dict_ensembl = f.ensembl("info/assembly/" + specie)
                karyotype_list = dict_ensembl["karyotype"]
                contents = f.read_html_file("karyotype.html") \
                    .render(context={
                    "karyotype": karyotype_list
                })
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()
        elif path == "/chromosomeLength":
            try:
                species = arguments["specie"][0]
                chromo = arguments["chromo"][0]
                dict_ensembl = f.ensembl("info/assembly/" + species)
                chromo_length = ""
                for d in dict_ensembl["top_level_region"]:
                    if d["name"] == chromo:
                        chromo_length = d["length"]
                if chromo_length != "":
                    contents = f.read_html_file("chromosomeLength.html") \
                        .render(context={
                        "chromoLength": chromo_length
                    })
                else:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()
        else:
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
        print("Stopped by the user")
        httpd.server_close()
