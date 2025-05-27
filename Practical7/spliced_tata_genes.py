import re

# Read the FASTA file and return a dictionary with the key as the gene name and the value as the sequence
def read_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        current_gene = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                 # Extract gene names
                current_gene = line.split()[0][1:]  # Retain only the gene name
                sequences[current_gene] = ""
            else:
                 # Splice sequences
                sequences[current_gene] += line
    return sequences

# Statistics Number of TATA boxes in the sequence
def count_tata_boxes(sequence):
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    return len(tata_pattern.findall(sequence))

# Screening genes by splice site and TATA box
def filter_spliced_genes(sequences, splice_pattern):
    spliced_genes = {}
    splice_regex = re.compile(splice_pattern)
    
    for gene, seq in sequences.items():
        if splice_regex.search(seq): # Check if the sequence contains splice sites
            tata_count = count_tata_boxes(seq) # Check if the sequence contains TATA box
            if tata_count > 0:
                spliced_genes[gene] = (tata_count, seq)
    
    return spliced_genes

def write_fasta(output_filename, spliced_genes):
    with open(output_filename, 'w') as file:
        for gene, (tata_count, seq) in spliced_genes.items():
            file.write(f'>{gene} | TATA count: {tata_count}\n{seq}\n')

# get input
splice_input = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ")
splice_patterns = {"GTAG": r'GT.*?AG', "GCAG": r'GC.*?AG', "ATAC": r'AT.*?AC'}

if splice_input not in splice_patterns:
    print("Invalid input. Please enter one of: GTAG, GCAG, ATAC")
    exit()

# Read the original FASTA file
fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
sequences = read_fasta(fasta_file)

# Screening for genes containing both splice sites and TATA boxes
filtered_spliced_genes = filter_spliced_genes(sequences, splice_patterns[splice_input])

#  Generating Output Files
output_file = f"{splice_input}_spliced_genes.fa"
write_fasta(output_file, filtered_spliced_genes)

print(f"Spliced genes with TATA box saved to {output_file}")