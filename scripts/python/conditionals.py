# conditionals.py
# Decision-making in Python — applied to biological sequences
# Winner Kubeyinje — Week 3, Day 3

def classify_gc(sequence):
    gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100

    if gc > 60:
        return "High GC — possible contamination or GC-rich organism"
    elif gc < 40:
        return "Low GC — AT-rich sequence, check for bias"
    else:
        return "Normal GC range — sequence looks typical"

# Test with three sequences
seq_normal = "ATCGATCGTAGCTAGCTAGCATCG"
seq_high   = "GCGCGCGCGCGCGCGCGCGCGCGC"
seq_low    = "ATATATATATATATATATATAT"

print("seq_normal:", classify_gc(seq_normal))
print("seq_high:", classify_gc(seq_high))
print("seq_low:", classify_gc(seq_low))


# --- Task 2: Sequence length classifier ---

def classify_length(sequence):
    length = len(sequence)
    
    if length < 50:
        return "Short sequence — possibly a primer or probe"
    elif length < 500:
        return "Medium sequence — could be a gene fragment"
    else:
        return "Long sequence — likely a full gene or genomic region"

# Create three test sequences
seq_short  = "ATCGATCGTAGCTAGCTA"       # 18 bases (< 50)
seq_medium = "ATCG" * 25                # 100 bases (between 50 and 499)
seq_long   = "ATCG" * 130               # 520 bases (>= 500)

# Call classify_length on each and print
print("seq_short:", classify_length(seq_short))
print("seq_medium:", classify_length(seq_medium))
print("seq_long:", classify_length(seq_long))

