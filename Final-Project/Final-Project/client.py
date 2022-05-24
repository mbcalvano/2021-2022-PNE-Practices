import http.client
import json
import termcolor


SERVER = "localhost:8080"
PARAMS = "json=1"

conn = http.client.HTTPConnection(SERVER)


try:
    # listSpecies endpoint
    conn.request("GET", "/listSpecies?limit=10&" + PARAMS)
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    termcolor.cprint("\nLIST SPECIES ENDPOINT", 'green')
    print("Number of species selected:", data1["n_species"])
    print("Number of species available:", data1["total_species"])
    print("List of species:")
    print(*data1["list_species"], sep=', ')

    # karyotype endpoint
    conn.request("GET", "/karyotype?specie=mouse&" + PARAMS)
    r2 = conn.getresponse()
    data2 = r2.read().decode("utf-8")
    data2 = json.loads(data2)
    termcolor.cprint("\nKARYOTYPE ENDPOINT", 'green')
    print("List of karyotypes:")
    print(*data2["karyotype"], sep=', ')

    # chromosomeLength endpoint
    conn.request("GET", "/chromosomeLength?specie=mouse&chromo=18&" + PARAMS)
    r3 = conn.getresponse()
    data3 = r3.read().decode("utf-8")
    data3 = json.loads(data3)
    termcolor.cprint("\nCHROMOSOME LENGTH ENDPOINT", 'green')
    print("The length of the chromosome is:", data3["chromoLength"])

    # geneSeq endpoint
    conn.request("GET", "/geneSeq?gene=FRAT1&" + PARAMS)
    r4 = conn.getresponse()
    data4 = r4.read().decode("utf-8")
    data4 = json.loads(data4)
    termcolor.cprint("\nGENE SEQ ENDPOINT", 'green')
    print("The sequence of the gene is:", data4["gene_seq"])

    # geneInfo endpoint
    conn.request("GET", "/geneInfo?gene=FRAT1&" + PARAMS)
    r5 = conn.getresponse()
    data5 = r5.read().decode("utf-8")
    data5 = json.loads(data5)
    termcolor.cprint("\nGENE INFO ENDPOINT", 'green')
    print("Gene:", data5["gene_name"])
    print("ID:", data5["gene_id"])
    print("Start:", data5["start"])
    print("End:", data5["end"])
    print("Length:", data5["gene_len"])
    print("Chromosome name:", data5["chromo_name"])

    # geneCalc endpoint
    conn.request("GET", "/geneCalc?gene=FRAT1&" + PARAMS)
    r6 = conn.getresponse()
    data6 = r6.read().decode("utf-8")
    data6 = json.loads(data6)
    termcolor.cprint("\nGENE CALC ENDPOINT", 'green')
    print("Gene:", data6["gene_name"])
    print("Length:", data5["gene_len"])
    print(data6["percentage"])

    # geneList endpoint
    conn.request("GET", "/geneList?chromo=9&start=22125500&end=22136000&" + PARAMS)
    r7 = conn.getresponse()
    data7 = r7.read().decode("utf-8")
    data7 = json.loads(data7)
    termcolor.cprint("\nGENE LIST ENDPOINT", 'green')
    print("List of genes:")
    for g in data7["list_genes"]:
        print("-" + g)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
