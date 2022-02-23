import Seq0
FOLDER = "../Session-04/"
list_bases = ["A", "C", "T", "G"]
list_genes = ["U5", "ADA", "FRAT1", "FXN"]
bases_count = []

for g in list_genes:
    print("Gene " + g + ":")
    seq = Seq0.seq_read_fasta(FOLDER + g + ".txt")
    for b in list_bases:
        bases_count.append(Seq0.seq_count_base(seq, b))