import http.client
from pathlib import Path
import json
import jinja2 as j

FOLDER = "html/"
SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

def read_html_file(filename):
    contents = Path(FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def ensembl(endpoint):
    try:
        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", endpoint + PARAMS)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")
        data1 = r1.read().decode("utf-8")
        return json.loads(data1)
    except ConnectionRefusedError:
        print("ERROR")
        return None

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, round((v * 100) / total, 2)]
    return d


def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" +"\n"
    return message


