# orf_finder.py
# Scans 3 forward reading frames to identify Open Reading Frames (ORFs) and extracts the longest coding sequence
# Winner Kubeyinje — Week 4, Day 4

"""
================================================================================
                           ALGORITHMIC OVERVIEW
================================================================================
Today's Objective:
1. Validate the raw DNA sequence to verify that all bases are clean (A, C, G, T).
2. Scan the 3 forward reading frames (offsets 0, 1, and 2) using a "Light Switch"
   state machine to detect every gene that starts with ATG and ends with a STOP codon.
3. Package all discovered ORFs into dictionary cards containing their coordinates,
   frame number, nucleotide length, and sequence.
4. Use the Chapter 5 Maximum Loop Pattern to identify the Longest ORF (The Champion).
5. Translate that Champion ORF into an amino acid protein sequence.
6. Print the summary to the screen and write a clean report to data/raw/orf_summary.txt.
================================================================================
"""

# ==============================================================================
# STAGE 1: THE FACTORY TOOLS (Definitions, Tables & Functions)
# ==============================================================================

# The 64-Codon Genetic Code Dictionary
# Maps each 3-base DNA triplet to its single-letter amino acid (or '*' for Stop)
CODON_TABLE = {
    # Phenylalanine (F) & Leucine (L)
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    # Leucine (L)
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    # Isoleucine (I) & Methionine (M - Start Codon)
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    # Valine (V)
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    # Serine (S)
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    # Proline (P)
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Threonine (T)
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    # Alanine (A)
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Tyrosine (Y) & Stop Codons (*)
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    # Histidine (H) & Glutamine (Q)
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    # Asparagine (N) & Lysine (K)
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    # Aspartate (D) & Glutamate (E)
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    # Cysteine (C), Tryptophan (W) & Stop Codon (*)
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    # Arginine (R)
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    # Serine (S) & Arginine (R)
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    # Glycine (G)
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# Boundary Codons in Molecular Biology
START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]


# Tool 1: Sequence Validation (Input Quality Control)
def validate_dna(sequence):
    """
    Counts the occurrence of standard nucleotides (A, C, G, T)
    and flags any ambiguous or unexpected characters (such as 'N').
    """
    valid_bases = {"A", "C", "G", "T"}
    base_counts = {"A": 0, "C": 0, "G": 0, "T": 0, "ambiguous": 0}

    # Loop through every single character in the sequence string
    for base in sequence:
        if base in valid_bases:
            base_counts[base] += 1
        else:
            base_counts["ambiguous"] += 1

    return base_counts


# Tool 2: Multi-line FASTA Parser (Re-used from Week 4 Day 2 & Day 3)
def parse_fasta(filepath):
    """
    Reads a multi-line wrapped FASTA file and returns a dictionary
    mapping each sequence header ID to its continuous DNA sequence.
    """
    sequences = {}
    current_id = None
    current_seq = []

    # Open file using Python's standard file-reading pattern (Chapter 7)
    with open(filepath, "r") as file_handle:
        for line in file_handle:
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Header lines start with '>'
            if line.startswith(">"):
                # If we were already holding a sequence, save it before moving on
                if current_id is not None:
                    sequences[current_id] = "".join(current_seq).upper()

                # Extract the sequence ID (e.g. '>seq_001 BRCA1' becomes 'seq_001')
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                # Accumulate multi-line wrapped sequence chunks
                current_seq.append(line)

        # Save the final sequence after reaching the end of the file
        if current_id is not None:
            sequences[current_id] = "".join(current_seq).upper()

    return sequences


# Tool 3: Single-Frame ORF Scanner (The Light Switch State Machine)
def find_orfs_in_frame(sequence, frame_offset):
    """
    Scans ONE reading frame (frame_offset: 0, 1, or 2) in steps of 3.
    Uses a Boolean flag (inside_orf) to track when we are inside an active gene.
    """
    found_orfs = []
    inside_orf = False
    start_index = None

    # Step in triplets from the frame offset up to the last complete codon
    # len(sequence) - 2 ensures we always have at least 3 bases to slice
    for i in range(frame_offset, len(sequence) - 2, 3):
        codon = sequence[i : i + 3]

        if not inside_orf:
            # We are hunting for the start of a gene
            if codon == START_CODON:
                inside_orf = True
                start_index = i
        else:
            # We are inside an active gene, hunting for a stop codon
            if codon in STOP_CODONS:
                # i + 3 captures all 3 letters of the stop codon
                end_index = i + 3
                orf_seq = sequence[start_index : end_index]

                # Package all facts about this ORF into a dictionary record
                record = {
                    "frame": frame_offset + 1,       # Biological frame numbering (1, 2, 3)
                    "start": start_index + 1,        # 1-based biological coordinate
                    "end": end_index,                # 1-based biological coordinate
                    "length_nt": len(orf_seq),       # Nucleotide length
                    "length_aa": len(orf_seq) // 3,  # Amino acid length
                    "dna_seq": orf_seq               # Complete coding sequence
                }
                found_orfs.append(record)

                # Reset switch: ready to discover the next gene further down the strand
                inside_orf = False

    return found_orfs


# Tool 4: Multi-Frame ORF Scanner
def find_all_orfs(sequence):
    """
    Iterates through all 3 forward frames (offsets 0, 1, 2)
    and combines all discovered candidate ORFs into a single list.
    """
    all_orfs = []
    for frame_offset in [0, 1, 2]:
        frame_orfs = find_orfs_in_frame(sequence, frame_offset)
        all_orfs.extend(frame_orfs)
    return all_orfs


# Tool 5: Codon Translation Engine (Re-used from Week 4 Day 3)
def translate_dna(sequence):
    """
    Translates an ORF nucleotide sequence into an amino acid peptide string.
    Uses .get(codon, 'X') to safely handle unknown codons.
    """
    peptide = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i : i + 3]
        amino_acid = CODON_TABLE.get(codon, "X")
        peptide.append(amino_acid)
    return "".join(peptide)


# ==============================================================================
# STAGE 2: THE SUPPLY LINE (File Paths)
# ==============================================================================

input_file = "data/fasta/gene.fna"
output_file = "data/raw/orf_summary.txt"


# ==============================================================================
# STAGE 3: RUNNING THE PIPELINE (Pure Linear Execution)
# ==============================================================================

print("=" * 70)
print("      WEEK 4 DAY 4: OPEN READING FRAME (ORF) FINDER & SCANNER")
print("=" * 70)

# Step 1: Load sequence from FASTA file
print(f"\n[Step 1] Loading FASTA dataset: {input_file}")
records = parse_fasta(input_file)
seq_id = list(records.keys())[0]
sequence = records[seq_id]
total_len = len(sequence)

print(f" -> Sequence ID: {seq_id}")
print(f" -> Total sequence length: {total_len:,} nucleotides")

# Step 2: Validate sequence composition
print(f"\n[Step 2] Validating sequence composition...")
counts = validate_dna(sequence)
print(f" -> A: {counts['A']:,} | C: {counts['C']:,} | G: {counts['G']:,} | T: {counts['T']:,}")
if counts["ambiguous"] > 0:
    print(f" -> Ambiguous bases detected: {counts['ambiguous']:,}")
else:
    print(" -> Data Quality: 100% standard nucleotides (A, C, G, T). Clean for ORF search.")

# Step 3: Scan all 3 forward reading frames
print(f"\n[Step 3] Scanning 3 forward reading frames for Start -> Stop windows...")
all_orfs = find_all_orfs(sequence)
print(f" -> Total candidate ORFs discovered: {len(all_orfs):,}")

# Breakdown counts by frame
frame_counts = {1: 0, 2: 0, 3: 0}
for orf in all_orfs:
    frame_counts[orf["frame"]] += 1

print(f"    - Frame 1: {frame_counts[1]:,} candidate ORFs")
print(f"    - Frame 2: {frame_counts[2]:,} candidate ORFs")
print(f"    - Frame 3: {frame_counts[3]:,} candidate ORFs")

# Step 4: Extract the Longest ORF (Chapter 5 Maximum Loop Pattern)
print(f"\n[Step 4] Extracting the Longest ORF (The Gene Champion)...")
longest_orf = None
max_length = 0

for orf in all_orfs:
    if orf["length_nt"] > max_length:
        max_length = orf["length_nt"]
        longest_orf = orf

# Step 5: Translate the Champion ORF into protein
protein_seq = translate_dna(longest_orf["dna_seq"])

# Step 6: Print detailed scientific findings to the screen
print(f"\n" + "-" * 70)
print("                    LONGEST ORF IDENTIFIED")
print("-" * 70)
print(f"Reading Frame:          Frame {longest_orf['frame']}")
print(f"Start Position:         Base {longest_orf['start']:,}")
print(f"End Position:           Base {longest_orf['end']:,}")
print(f"Nucleotide Length:      {longest_orf['length_nt']:,} bp")
print(f"Protein Length:         {longest_orf['length_aa']:,} amino acids")
print(f"First 10 Codons:        {longest_orf['dna_seq'][:30]}")
print(f"First 10 Amino Acids:   {protein_seq[:10]}")
print(f"Terminal Codon:         {longest_orf['dna_seq'][-3:]} (Stop: '{protein_seq[-1]}')")
print("-" * 70)

# Step 7: Export structured report to data/raw/orf_summary.txt
print(f"\n[Step 7] Writing structured summary report to: {output_file}")
with open(output_file, "w") as out_f:
    out_f.write("=" * 70 + "\n")
    out_f.write("         OPEN READING FRAME (ORF) ANALYSIS REPORT\n")
    out_f.write("=" * 70 + "\n\n")
    out_f.write(f"Sequence ID:             {seq_id}\n")
    out_f.write(f"Total Sequence Length:   {total_len:,} bp\n")
    out_f.write(f"Total ORFs Discovered:   {len(all_orfs):,}\n")
    out_f.write(f"Frame 1 Count:           {frame_counts[1]:,}\n")
    out_f.write(f"Frame 2 Count:           {frame_counts[2]:,}\n")
    out_f.write(f"Frame 3 Count:           {frame_counts[3]:,}\n\n")
    out_f.write("-" * 70 + "\n")
    out_f.write("CHAMPION (LONGEST) ORF DETAILS\n")
    out_f.write("-" * 70 + "\n")
    out_f.write(f"Frame:                   Frame {longest_orf['frame']}\n")
    out_f.write(f"Start Coordinate:        {longest_orf['start']:,}\n")
    out_f.write(f"End Coordinate:          {longest_orf['end']:,}\n")
    out_f.write(f"Nucleotide Length:       {longest_orf['length_nt']:,} bp\n")
    out_f.write(f"Amino Acid Length:       {longest_orf['length_aa']:,} aa\n\n")
    out_f.write("Nucleotide Sequence (first 120 bp):\n")
    out_f.write(longest_orf["dna_seq"][:120] + "...\n\n")
    out_f.write("Translated Protein Sequence:\n")
    out_f.write(protein_seq + "\n\n")
    out_f.write("=" * 70 + "\n")
    out_f.write("TOP 10 LONGEST ORFs DISCOVERED\n")
    out_f.write("=" * 70 + "\n")
    out_f.write("Rank\tFrame\tStart\tEnd\tLength(nt)\tLength(aa)\n")

    # Sort all ORFs by nucleotide length descending to show the top 10
    sorted_orfs = sorted(all_orfs, key=lambda x: x["length_nt"], reverse=True)
    for rank, orf in enumerate(sorted_orfs[:10], start=1):
        out_f.write(f"{rank}\tFrame {orf['frame']}\t{orf['start']}\t{orf['end']}\t{orf['length_nt']}\t{orf['length_aa']}\n")

print(f" -> Successfully saved report to {output_file}!")
print("\n" + "=" * 70)
print("      EXECUTION COMPLETE")
print("=" * 70)