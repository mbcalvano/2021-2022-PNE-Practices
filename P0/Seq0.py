def seq_ping():
    print("OK")

def ask_for_file(FOLDER):
    exit = False
    while not exit:
        filename = FOLDER + input("DNA file: ") + ".txt"
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File was not found. Try again")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base(seq, base):
    count = 0
    count = seq.count(base)
    return count

def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    list_bases = ["A", "T", "C", "G"]
    for b in list_bases:
        d[b] = seq.count(b)
    return d

def seq_reverse(seq):
    inverse_seq = seq[::-1]
    return inverse_seq

def seq_complement(seq):
    d = {'A': "T", 'T': "A", 'C': "G", 'G': "C"}
    dna_complement = ""
    for l in seq:
        dna_complement += d[l]
    return dna_complement