import Seq0
FOLDER = "../Session-04/"
FILENAME = "U5.txt"
filename = Seq0.ask_for_file()
sequence = Seq0.seq_read_fasta(filename)
print("The first 20 sequences are:")
print(sequence[:20])



