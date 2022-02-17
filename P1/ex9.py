from seq1 import Seq
FOLDER = "../Session-04/"
FILENAME = "U5"

s = Seq()
s.read_fasta(FOLDER + FILENAME + ".txt")

print(f"Sequence: (Length: {Seq.len(s)}) {s}", sep="")
print(f" Bases: {Seq.count(s)}")
print(f" Rev: {Seq.reverse(s)}")
print(f" Comp: {Seq.complement(s)}")