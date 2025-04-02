import re

def read_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        current_gene = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_gene = line[1:]  # remove '>'
                sequences[current_gene] = ""
            else:
                sequences[current_gene] += line
    return sequences

def count_tata_boxes(sequence):
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    return len(tata_pattern.findall(sequence))

def filter_spliced_genes(sequences, splice_pattern):
    spliced_genes = {}
    splice_regex = re.compile(splice_pattern)
    
    for gene, seq in sequences.items():
        if splice_regex.search(seq):
            tata_count = count_tata_boxes(seq)
            spliced_genes[gene] = (tata_count, seq)
    
    return spliced_genes

def write_fasta(output_filename, spliced_genes):
    with open(output_filename, 'w') as file:
        for gene, (tata_count, seq) in spliced_genes.items():
            file.write(f'>{gene} | TATA count: {tata_count}\n{seq}\n')

# Get user input
splice_input = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ")
splice_patterns = {"GTAG": r'GT.*?AG', "GCAG": r'GC.*?AG', "ATAC": r'AT.*?AC'}

if splice_input not in splice_patterns:
    print("Invalid input. Please enter one of: GTAG, GCAG, ATAC")
    exit()

# Read TATA gene FASTA file
tata_fasta_file = "tata_genes.fa"
sequences = read_fasta(tata_fasta_file)

# Screening for genes matching splice sites
filtered_spliced_genes = filter_spliced_genes(sequences, splice_patterns[splice_input])

# Generating output files
tata_spliced_output = f"{splice_input}_spliced_genes.fa"
write_fasta(tata_spliced_output, filtered_spliced_genes)

print(f"Spliced genes with TATA box saved to {tata_spliced_output}")
