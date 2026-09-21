# dictionaries.py
# Dictionaries and biological lookup tables
# Winner Kubeyinje — Week 4, Day 1

# The complement dictionary — Chargaff's rules in code
complement_map = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

def get_complement(sequence):
    """Return the complement of a DNA sequence."""
    result = ""
    for base in sequence:
        result = result + complement_map[base]
    return result

def get_reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    comp = get_complement(sequence)
    return comp[::-1]    # this reverses a string — new syntax!

# Test sequences
seq1 = "ATCG"
seq2 = "ATCGATCGTAGCTAGC"

print(f"Original:           {seq1}")
print(f"Complement:         {get_complement(seq1)}")
print(f"Reverse complement: {get_reverse_complement(seq1)}")
print()
print(f"Original:           {seq2}")
print(f"Complement:         {get_complement(seq2)}")
print(f"Reverse complement: {get_reverse_complement(seq2)}")

# --- Nucleotide frequency counter ---
def nucleotide_frequency(sequence):
    """Count each nucleotide and return as a dictionary."""
    freq = {}
    for base in sequence:
        if base in freq:
            freq[base] = freq[base] + 1
        else:
            freq[base] = 1
    return freq

test_seq = "ATCGATCGTAGCTAGCTAGCATCG"
frequencies = nucleotide_frequency(test_seq)

print("\n=== Nucleotide Frequencies ===")
for base, count in frequencies.items():
    percentage = count / len(test_seq) * 100
    print(f"{base}: {count} ({percentage:.1f}%)")