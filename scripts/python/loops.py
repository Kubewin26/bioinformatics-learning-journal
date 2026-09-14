# loops.py
# Loops and lists — processing multiple sequences
# Winner Kubeyinje — Week 3, Day 4

# A list of DNA sequences to analyse
sequences = [
    "ATCGATCGTAGCTAGCTAGCATCG",
    "GCGCGCGCGCGCGCGCGCGCGCGC",
    "ATATATATATATATATATATAT",
    "ATCGATCGATCGATCGATCGATCG",
    "GCATGCATGCATGCATGCATGCAT"
]

# Loop over every sequence and calculate metrics
print("=== GC Content Analysis ===")
for seq in sequences:
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    print("Sequence:", seq[:10], "... | Length:", len(seq), "| GC:", gc, "%")


    # --- Task 2: Loop + classify_gc combined ---

def classify_gc(sequence):
    gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
    if gc > 60:
        return "High GC"
    elif gc < 40:
        return "Low GC"
    else:
        return "Normal GC"

print("\n=== Sequence Classification Report ===")
for i, seq in enumerate(sequences):
    classification = classify_gc(seq)
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    print(f"Seq {i+1}: {classification} ({gc}%) — Length: {len(seq)} bp")
    