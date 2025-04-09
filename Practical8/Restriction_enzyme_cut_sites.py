def find_cut_sites(dna_seq, enzyme_seq):
    if not set(dna_seq).issubset({'A', 'C', 'G', 'T'}) or not set(enzyme_seq).issubset({'A', 'C', 'G', 'T'}):
        return "Error: Sequences must contain only A, C, G, T."
    #  the sequence recognised by the restriction enzyme and then find the positions
    positions = []
    for i in range(len(dna_seq) - len(enzyme_seq) + 1):
        if dna_seq[i:i+len(enzyme_seq)] == enzyme_seq:
            positions.append(i)
    return positions

# Example call
print(find_cut_sites("AAGCTGAAGCTTCAAGCTTCCG", "AAGCTT")) # Positions are numbered from zero and the first nucleotide in the sequence is at position “0”