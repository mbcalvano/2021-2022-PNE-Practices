import Seq0
FOLDER = "../Session-04/"

list_genes = ["U5", "ADA", "FRAT1", "FXN"]

for g in list_genes:
    seq = Seq0.seq_read_fasta(FOLDER + g + ".txt")
    print("Gene ", g, ": ", Seq0.seq_count(seq), sep="")
