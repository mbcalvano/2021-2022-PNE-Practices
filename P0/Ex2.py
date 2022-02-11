import Seq0
FOLDER = "../Session-04/"
filename = Seq0.ask_for_file(FOLDER)
sequence = Seq0.seq_read_fasta(filename)
print("The first 20 sequences are:")
print(sequence[:20])



