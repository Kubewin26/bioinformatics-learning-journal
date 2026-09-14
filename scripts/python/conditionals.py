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
