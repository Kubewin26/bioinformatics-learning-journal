# functions.py
# Defining and calling functions
# Winner Kubeyinje — Week 3, Day 2

def calculate_gc(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    gc = (g + c) / len(sequence) * 100
    return gc

# Three test sequences
seq1 = "ATCGATCG"
seq2 = "GCGCGCGC"
seq3 = "ATATATATAT"

print("GC of seq1:", calculate_gc(seq1))
print("GC of seq2:", calculate_gc(seq2))
print("GC of seq3:", calculate_gc(seq3))
