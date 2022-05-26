from seq1 import Seq
import http.client
import json

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

def most_frequent(s):
    d = s.count()
    largest = 0
    for k,v in d.items():
        if v > largest:
            largest = v
            base = k
    return base

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"

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
gene = input("Write the gene name: ")
print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + genes_dict[gene] + PARAMS)
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    # -- Print the received data
    print("Gene:", gene)
    print("Description:", data1["desc"])
    s = Seq(data1["seq"])
    print(info(s))
    print("Most frequent base:", most_frequent(s))
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
except KeyError:
    print("Please enter a valid gene")
