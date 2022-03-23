class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.null_sequence():
            print("NULL Seq created")
        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")
        else:
            print("New sequence created!")

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

    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def read_fasta(self, filename):
        seq = open(filename, "r").read()
        self.strbases = seq[seq.find("\n"):].replace("\n", "")

    def len(self):
        """Calculate the length of the sequence"""
        if self.null_sequence() or not self.valid_sequence():
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
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

    def count(self):
        if self.null_sequence():
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
            list_bases = ["A", "C", "G", "T"]
            try:
                for b in list_bases:
                    d[b] = self.strbases.count(b)
                return d
            except KeyError:
                return d

    def reverse(self):
        if self.null_sequence():
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            inverse_seq = self.strbases[::-1]
            return inverse_seq

    def complement(self):
        if self.null_sequence():
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            d = {'A': "T", 'T': "A", 'C': "G", 'G': "C"}
            dna_complement = ""
            for l in self.strbases:
                dna_complement += d[l]
            return dna_complement
