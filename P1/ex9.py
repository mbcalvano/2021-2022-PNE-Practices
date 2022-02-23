from seq1 import Seq
FOLDER = "../Session-04/"
FILENAME = "U5"

s = Seq()
s.read_fasta(FOLDER + FILENAME + ".txt")

print(f"Sequence: (Length: {s.len()}) {s}", sep="")
print(f" Bases: {s.count()}")
print(f" Rev: {s.reverse()}")
print(f" Comp: {s.complement()}")