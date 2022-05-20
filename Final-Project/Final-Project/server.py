import http.server
import socketserver
import termcolor
from urllib.parse import parse_qs, urlparse
import functions as f
import pathlib
from class_seq import Seq

PORT = 8080
FOLDER = "html/"
SERVER = "rest.ensembl.org"
ARGUMENT = "?content-type=application/json"

genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207588",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"
              }

genes_list = ["SRCAP", "FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]

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
            contents = f.read_html_file("index.html") \
                .render(context={
                "genes": genes_list
            })
        elif path == "/listSpecies":
            try:
                dict_ensembl = f.ensembl("/info/species?")
                list_species = []
                total_species = len([ele for ele in dict_ensembl["species"] if isinstance(ele, dict)])
                try:
                    n_species = int(arguments["limit"][0])
                except KeyError:
                    n_species = total_species
                for i in range(n_species):
                    list_species.append(dict_ensembl["species"][i]["display_name"])
                print(n_species)
                if list_species[0] != "":
                    contents = f.read_html_file("listSpecies.html") \
                        .render(context={
                        "n_species": n_species,
                        "list_species": list_species,
                        "total_species": total_species
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
                dict_ensembl = f.ensembl("info/assembly/" + specie.replace(" ", "") + "?")
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
                dict_ensembl = f.ensembl("info/assembly/" + species + "?")
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
        elif path == "/geneSeq" or path == "/geneInfo" or path == "/geneCalc":
            gene_name = arguments["gene_name"][0]
            gene_id = genes_dict[gene_name]
            dict_ensembl = f.ensembl("sequence/id/" + gene_id + "?")
            gene_seq = dict_ensembl["seq"]
            if path == "/geneSeq": contents = f.read_html_file("geneSeq.html") \
                .render(context={
                "gene_seq": gene_seq
            })
            elif path == "/geneInfo":
                desc_list = dict_ensembl["desc"].split(":")
                chromo_name = desc_list[2]
                start = desc_list[3]
                end = desc_list[4]
                s = Seq(gene_seq)
                gene_len = s.len()
                contents = f.read_html_file("geneInfo.html") \
                    .render(context={
                    "gene_name": gene_name,
                    "start": start,
                    "end": end,
                    "chromo_name": chromo_name,
                    "gene_len": gene_len,
                    "gene_id": gene_id
                })
            elif path == "/geneCalc":
                s = Seq(gene_seq)
                base_count = s.count_percentage()
                gene_len = s.len()
                contents = f.read_html_file("geneCalc.html") \
                    .render(context={
                    "gene_name": gene_name,
                    "gene_seq": gene_seq,
                    "gene_len": gene_len,
                    "percentage": f.convert_message(base_count)
                })
        elif path == "/geneList":
            try:
                chromosome = int(arguments["chromosome"][0])
                start = int(arguments["start"][0])
                end = int(arguments["end"][0])
                if start < end:
                    dict_list_ensembl = f.ensembl("phenotype/region/homo_sapiens/" + str(chromosome) + ":" + str(start) + "-" + str(end) + "?feature_type=Variation;")
                    list_genes = []
                    for d in dict_list_ensembl:
                        if "phenotype_associations" in d.keys():
                            for di in d["phenotype_associations"]:
                                if "attributes" in di.keys():
                                    if "associated_gene" in di["attributes"]:
                                        list_genes.append(di["attributes"]["associated_gene"])
                    contents = f.read_html_file("geneList.html") \
                        .render(context={
                        "list_genes": list_genes
                    })
                else:
                    contents = pathlib.Path("html/error.html").read_text()
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()
            except AttributeError:
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
