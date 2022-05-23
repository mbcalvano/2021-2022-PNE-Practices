import http.client
import json


SERVER = "localhost:8080"
PARAMS = "json=1"

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", "listSpecies?limit=&" + PARAMS)
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(data1)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
