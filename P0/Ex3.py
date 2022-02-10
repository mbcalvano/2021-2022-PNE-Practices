import Seq0

FOLDER = "../Session-04/"

list_genes = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_genes:
    print("Gene", l, "---> Length:", len(Seq0.seq_read_fasta(FOLDER + l + ".txt")))