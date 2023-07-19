class GeneSequenceComparer:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

    def compare_sequences(self):
        zip_seqs = zip(self.seq1, self.seq2)
        zip_seqs = list(zip_seqs)

        enum_seqs = list(enumerate(zip_seqs))

        comparison_results = ""
        for i, (a, b) in enum_seqs:
            if a != b:
                if len(a) == len(b):
                    mutation_type = 'Substitution'
                elif len(a) > len(b):
                    mutation_type = 'Deletion'
                else:
                    mutation_type = 'Insertion'

                comparison_results += f'index: {i}, a: {a}, b: {b}  <- Highlighted, Mutation Type: {mutation_type}\n'
            else:
                comparison_results += f'index: {i}, a: {a}, b: {b}\n'

        return comparison_results
