import Seq0
FOLDER = "../Session-04/"

list_genes = ["U5", "ADA", "FRAT1", "FXN"]

for g in list_genes:
    seq = Seq0.seq_read_fasta(FOLDER + g + ".txt")
    dictionary = Seq0.seq_count(seq)
    print("Gene ", g, ": Most frequent Base: ", max(dictionary, key=dictionary.get), sep="")
