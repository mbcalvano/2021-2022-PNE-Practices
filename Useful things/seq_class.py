class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if self.null_sequence():
            print("NULL Seq created")
        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")
        else:
            print("New sequence created!")

    def __str__(self):
        return self.strbases

    def null_sequence(self):
        null = False
        if self.strbases == "NULL":
            null = True
        return null

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def read_fasta(self, filename):
        """Opens and formats a fasta file"""
        seq = open(filename, "r").read()
        self.strbases = seq[seq.find("\n"):].replace("\n", "")

    def len(self):
        """Calculate the length of the sequence"""
        if self.null_sequence() or not self.valid_sequence():
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        """Returns a dictionary with the count of each base"""
        if self.null_sequence():
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            d = {"A": 0, "C": 0, "G": 0, "T": 0}
            try:
                for b in self.strbases:
                    d[b] += 1
                return d
            except KeyError:
                return d

    def reverse(self):
        """Returns the inverse of the dna sequence"""
        if self.null_sequence():
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            inverse_seq = self.strbases[::-1]
            return inverse_seq

    def complement(self):
        """Returns the complement of the dna sequence"""
        if self.null_sequence():
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            d = {'A': "T", 'T': "A", 'C': "G", 'G': "C"}
            dna_complement = ""
            for b in self.strbases:
                dna_complement += d[b]
            return dna_complement
