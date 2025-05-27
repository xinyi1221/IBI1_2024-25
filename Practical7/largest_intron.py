import re

def find_largest_intron(seq):
    # Regular expression matching introns between GT (donor site) and AG (acceptor site)
    introns = re.findall(r'(GT.*AG)', seq)  # This line of code looks for the largest intron from the first GT to the last AG.
                                            # Change this line of code to: introns = re.findall(r'(GT.*?AG)', seq) if largest intron means: the largest intron of all possible segments from each GT to the first AG thereafter
    
    if not introns:
        return 0, "No intron found"
    
    # Finding the longest intron
    largest_intron = max(introns, key=len)
    return len(largest_intron) , largest_intron  # The lengths of GT and AG have been added before

# A given DNA sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Calculate the longest intron
length, intron_seq = find_largest_intron(seq)

# output result
print(f"The length of the largest intron is: {length}")
print(f"Largest intron sequence: {intron_seq}")
