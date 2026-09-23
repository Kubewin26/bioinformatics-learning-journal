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