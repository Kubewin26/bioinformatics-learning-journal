# strings.py
# Strings operations and data types
# Winner Kubeyinje — Week 3, Day 2

# --- STRINGS ---
gene_name = "BRCA1"
organism = "Homo sapiens"
dna = "ATCGATCGTAGCTAGCTAGCATCG"

# String concatenation - joining strings with +
description = gene_name + " is found in " + organism
print(description)

# String length
print("Gene name length:", len(gene_name))
print("DNA sequence length:", len(dna))

# String slicing - extracting a portion of a string
# Syntax: string[start:end] - start is included, end is NOT (half-open interval)
first_codon = dna[0:3]  # Extracts "ATC"
second_codon = dna[3:6]  # Extracts "GAT"
print("First codon:", first_codon)
print("Second codon:", second_codon)

# String methods
print("Uppercase:", dna.upper())
print("Lowercase:", dna.lower())
print("G count:", dna.count("G"))

# --- DATA TYPES ---
sequence_length = len(dna)      # integer (int)
gc_fraction = 0.5               # decimal (float)
sequence_name = "test_seq_01"   # text (str)

print("Type of sequence_length:", type(sequence_length))
print("Type of gc_fraction:", type(gc_fraction))
print("Type of sequence_name:", type(sequence_name))

