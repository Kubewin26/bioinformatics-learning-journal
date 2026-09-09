# dna_basics.py
# Exploring a DNA sequence using Python basics
# Winner Kubeyinje — Week 3, Day 1

# Store a DNA sequence in a variable
dna_sequence = "ATCGATCGTAGCTAGCTAGCATCG"

# Print the sequence
print("DNA sequence:", dna_sequence)

# Find the length of the sequence
sequence_length = len(dna_sequence)
print("Length:", sequence_length, "bases")

# Count each nucleotide
count_A = dna_sequence.count("A")
count_T = dna_sequence.count("T")
count_G = dna_sequence.count("G")
count_C = dna_sequence.count("C")

print("A count:", count_A)
print("T count:", count_T)
print("G count:", count_G)
print("C count:", count_C)

# Calculate GC content
gc_content = (count_G + count_C) / sequence_length * 100
print("GC content:", gc_content, "%")