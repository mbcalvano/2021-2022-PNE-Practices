from seq1 import Seq
s0 = Seq()
s1 = Seq("ACTGA")
s2 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {Seq.len(s0)}) {s0}")
print(f"Sequence 1: (Length: {Seq.len(s1)}) {s1}")
print(f"Sequence 2: (Length: {Seq.len(s2)}) {s2}")