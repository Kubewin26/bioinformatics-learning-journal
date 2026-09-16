# week3_qc_pipeline.py
# Week 3 Mini-Project: Sequence Quality Control Pipeline
# Winner Kubeyinje — Week 3, Day 6
# Reads sequences from a file, calculates QC metrics,
# classifies each sequence, flags problems, writes report.

def calculate_gc(sequence):
    if len(sequence) == 0:
        return 0.0
    valid_bases = sequence.count("A") + sequence.count("T") + \
                  sequence.count("G") + sequence.count("C")
    if valid_bases == 0:
        return 0.0
    return (sequence.count("G") + sequence.count("C")) / len(sequence) * 100

def classify_gc(gc):
    if gc > 60:
        return "HIGH_GC"
    elif gc < 40:
        return "LOW_GC"
    else:
        return "NORMAL"

def classify_length(sequence):
    length = len(sequence)
    if length < 10:
        return "TOO_SHORT"
    elif length < 50:
        return "SHORT"
    else:
        return "ACCEPTABLE"

def flag_sequence(sequence, gc):
    if "N" in sequence:
        return "FAIL — contains ambiguous bases (N)"
    elif gc == 0.0:
        return "FAIL — zero GC content"
    elif gc == 100.0:
        return "FAIL — 100% GC content"
    else:
        return "PASS"

# --- Main pipeline ---
input_file  = "data/raw/test_sequences.txt"
output_file = "data/raw/qc_report.txt"

print("=== Week 3 QC Pipeline ===")
print(f"Input:  {input_file}")
print(f"Output: {output_file}")
print()

with open(output_file, "w") as out:
    # Write TSV header
    out.write("sequence\tlength\tgc_content\tgc_class\tlength_class\tstatus\n")

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Calculate metrics
            gc     = calculate_gc(line)
            gc_cls = classify_gc(gc)
            ln_cls = classify_length(line)
            status = flag_sequence(line, gc)

            # Print to screen
            print(f"{line[:12]}... | GC: {gc:.1f}% | {gc_cls} | {ln_cls} | {status}")

            # Write to file
            out.write(f"{line}\t{len(line)}\t{gc:.1f}\t{gc_cls}\t{ln_cls}\t{status}\n")

print()
print(f"QC report written to {output_file}")