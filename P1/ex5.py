from seq1 import Seq

s0 = Seq()
s1 = Seq("ACTGA")
s2 = Seq("Invalid sequence")

seq_list = [s0, s1, s2]

i = 0
for seq in seq_list:
    print("\nSequence ", i, f": (Length: {Seq.len(seq)}) {seq}", sep="")
    for k, v in Seq.count_base(seq).items():
        print(" ", k + ": ", v, ", ", end='', sep="")
    i += 1




