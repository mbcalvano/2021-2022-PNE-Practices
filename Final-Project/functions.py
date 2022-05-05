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

def format_list(list):
    content = ""
    for i in list:
        content += i + " \n "
    return content

