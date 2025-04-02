import re

def read_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        current_gene = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_gene = line.split()[0][1:]  # Retain only the gene name
                sequences[current_gene] = ""
            else:
                sequences[current_gene] += line
    return sequences

def find_tata_genes(sequences):
    tata_genes = {}
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    
    for gene, seq in sequences.items():
        if tata_pattern.search(seq):
            tata_genes[gene] = seq
    
    return tata_genes

def write_fasta(output_filename, tata_genes):
    with open(output_filename, 'w') as file:
        for gene, seq in tata_genes.items():
            file.write(f'>{gene}\n{seq}\n')

# Read the original FASTA file
fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
sequences = read_fasta(fasta_file)

# Identify genes containing TATA boxes
filtered_tata_genes = find_tata_genes(sequences)

# Write a new FASTA file
tata_output_file = "tata_genes.fa"
write_fasta(tata_output_file, filtered_tata_genes)

print(f"TATA box containing genes saved to {tata_output_file}")
