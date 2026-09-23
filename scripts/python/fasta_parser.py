# fasta_parser.py
# Parsing FASTA format files
# Winner Kubeyinje — Week 4, Day 2

def parse_fasta(filepath):
    """
    Parse a FASTA file and return a dictionary:
    keys = sequence IDs, values = sequences
    """
    sequences = {}
    current_id = None
    current_seq = ""

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                # Save the previous sequence before starting a new one
                if current_id is not None:
                    sequences[current_id] = current_seq

                # Start a new sequence
                current_id = line[1:].split()[0]  # grab ID only, skip >
                current_seq = ""
            else:
                current_seq = current_seq + line  # concatenate multi-line seqs

        # Don't forget the last sequence — no > after it to trigger the save
        if current_id is not None:
            sequences[current_id] = current_seq

    return sequences


# --- Run the parser ---
fasta_file = "data/fasta/test_sequences.fasta"
parsed = parse_fasta(fasta_file)

print("=== Parsed FASTA sequences ===")
for seq_id, sequence in parsed.items():
    print(f"ID: {seq_id}")
    print(f"  Length: {len(sequence)} bp")
    print(f"  First 12 bases: {sequence[:12]}")
    print()

# --- Combining FASTA Parser with QC Analysis ---

def calculate_gc(sequence):
    """Calculate GC percentage."""
    if len(sequence) == 0:
        return 0.0
    g = sequence.count("G")
    c = sequence.count("C")
    return round((g + c) / len(sequence) * 100, 1)

def classify_gc(gc):
    """Classify GC content into biological ranges."""
    if gc > 60.0:
        return "HIGH_GC"
    elif gc < 40.0:
        return "LOW_GC"
    else:
        return "NORMAL"

def flag_sequence(sequence, gc):
    """Flag problematic biological sequences."""
    if "N" in sequence:
        return "FAIL — contains ambiguous bases (N)"
    elif gc == 0.0:
        return "FAIL — 0% GC content"
    elif gc == 100.0:
        return "FAIL — 100% GC content"
    else:
        return "PASS"

print("\n=== FASTA Quality Control Report ===")
print(f"{'ID':<12}\t{'Length':<8}\t{'GC%':<6}\t{'Category':<10}\t{'QC Status'}")
print("-" * 65)

for seq_id, seq in parsed.items():
    gc = calculate_gc(seq)
    category = classify_gc(gc)
    status = flag_sequence(seq, gc)
    print(f"{seq_id:<12}\t{len(seq)} bp\t{gc}%\t{category:<10}\t{status}")