import Seq0
FOLDER = "../Session-04/"
GENE = "U5"

seq = Seq0.seq_read_fasta(FOLDER + GENE + ".txt")[:20]
print("Gene " + GENE + ":")
print("Frag:", seq)
print("Rev:", Seq0.seq_reverse(seq))