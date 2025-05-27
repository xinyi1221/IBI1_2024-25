# Define a function to read a FASTA file and return the sequence name and sequence
def read_fasta(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    name = lines[0].strip().lstrip('>')
    seq = ''.join(line.strip() for line in lines[1:])
    return name, seq

# Define a function to read the BLOSUM62 matrix from a file and return as a dictionary
def read_blosum62(file_path):
    with open(file_path) as f:
        lines = [line for line in f if not line.startswith('#')]
    headers = lines[0].split()
    matrix = {}
    for line in lines[1:]:
        parts = line.split()
        row_aa = parts[0]
        scores = list(map(int, parts[1:]))
        matrix[row_aa] = dict(zip(headers, scores))
    return matrix

# Define a function to compare two sequences:
#   - Calculate the alignment score using the BLOSUM62 matrix
#   - Calculate the percent identity
def compare_sequences(seq1, seq2, matrix):
    score = 0
    identity = 0
    for a, b in zip(seq1, seq2):
        score += matrix.get(a, {}).get(b, 0)  # score from BLOSUM62
        if a == b:
            identity += 1
    percent_identity = identity / len(seq1) * 100
    return score, percent_identity

# Load sequences
human_name, human_seq = read_fasta("human_sod2.fasta")
mouse_name, mouse_seq = read_fasta("mouse_sod2.fasta")
rand_name, rand_seq = read_fasta("random_seq.fasta")

# Load BLOSUM62 matrix
blosum62 = read_blosum62("blosum62.txt")

# Run comparisons
for (name1, seq1), (name2, seq2) in [
    ((human_name, human_seq), (mouse_name, mouse_seq)),
    ((human_name, human_seq), (rand_name, rand_seq)),
    ((mouse_name, mouse_seq), (rand_name, rand_seq)),
]:
    score, identity = compare_sequences(seq1, seq2, blosum62)
    print(f"{name1} vs {name2}")
    print(f"Score: {score}, Identity: {identity:.2f}%\n")
