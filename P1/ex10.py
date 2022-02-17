from seq1 import Seq
FOLDER = "../Session-04/"
s1 = Seq()
s2 = Seq()
s3 = Seq()
s4 = Seq()
s5 = Seq()
list_seq = [s1, s2, s3, s4, s5]
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

i = 0
for s in list_seq:
    s.read_fasta(FOLDER + list_genes[i] + ".txt")
    dictionary = Seq.count(s)
    print("Gene", list_genes[i] + f": Most frequent base:", max(dictionary, key=dictionary.get))
    i += 1