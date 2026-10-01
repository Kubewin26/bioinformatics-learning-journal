# six_frame_translator.py
# Translates a genomic locus across all 6 reading frames and exports a TSV summary
# Winner Kubeyinje — Week 4, Day 5

"""
================================================================================
                           ALGORITHMIC OVERVIEW
================================================================================
Goal:
1. Load the 22,267 bp locus from 'data/fasta/gene.fna'.
2. Calculate the overall GC content of the locus.
3. Generate the Reverse Complement strand (the opposite anti-parallel DNA strand).
4. Translate all 6 Reading Frames:
   - Forward Strand: Frame +1 (offset 0), Frame +2 (offset 1), Frame +3 (offset 2)
   - Reverse Strand: Frame -1 (offset 0), Frame -2 (offset 1), Frame -3 (offset 2)
5. For each frame:
   - Count the total amino acids and total stop codons (*).
   - Find the Longest Continuous Peptide (by splitting at '*' and picking the biggest piece).
6. Print a formatted summary table to the terminal.
7. Export a clean Tab-Separated Values (TSV) report to 'data/raw/six_frame_summary.tsv'.
================================================================================
"""

# ==============================================================================
# STAGE 1: THE FACTORY TOOLS (Dictionaries & Modular Functions)
# ==============================================================================

# Standard Genetic Code Dictionary (64 codons -> Amino Acids or '*')
CODON_TABLE = {
    # Phenylalanine (F) & Leucine (L)
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    # Leucine (L)
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    # Isoleucine (I) & Methionine (M - Start)
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

# Base complementation lookup table (From Week 4 Day 1)
COMPLEMENT_MAP = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}


# Tool 1: Multi-line FASTA Parser (From Week 4 Day 2)
def parse_fasta(filepath):
    """
    Reads a wrapped multi-line FASTA file and returns {header_id: full_sequence}.
    """
    sequences = {}
    current_id = None
    current_seq = []

    with open(filepath, "r") as file_handle:
        for line in file_handle:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_seq).upper()
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)

        if current_id is not None:
            sequences[current_id] = "".join(current_seq).upper()

    return sequences


# Tool 2: Reverse Complement Generator (From Week 4 Day 1)
def get_reverse_complement(sequence):
    """
    Generates the reverse complement of a DNA sequence.
    1. Replaces each base with its Watson-Crick complement partner.
    2. Reverses the entire string right-to-left using slicing [::-1].
    """
    complemented_bases = []
    for base in sequence:
        # Look up partner base; fallback to base itself if ambiguous
        complemented_bases.append(COMPLEMENT_MAP.get(base, base))

    # Join list into string and reverse it backwards
    return "".join(complemented_bases)[::-1]


# Tool 3: GC Content Calculator (From Week 3 QC Pipeline)
def calculate_gc(sequence):
    """
    Calculates GC content percentage: ((G + C) / total_length) * 100
    """
    if len(sequence) == 0:
        return 0.0
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    return round(((g_count + c_count) / len(sequence)) * 100, 2)


# Tool 4: Single Frame Translator (From Week 4 Day 3)
def translate_frame(sequence, offset):
    """
    Steps through a DNA sequence in triplets from a given offset (0, 1, or 2)
    and returns the complete translated protein sequence.
    """
    peptide = []
    for i in range(offset, len(sequence) - 2, 3):
        codon = sequence[i : i + 3]
        amino_acid = CODON_TABLE.get(codon, "X")
        peptide.append(amino_acid)
    return "".join(peptide)


# Tool 5: Longest Continuous Peptide Finder
def get_longest_peptide(protein_sequence):
    """
    Splits the translated protein wherever a stop codon '*' occurs,
    and returns the longest continuous piece of uninterrupted peptide.
    """
    # Splitting by '*' gives a list of all peptide fragments between stop signs
    fragments = protein_sequence.split("*")

    # Find the fragment with the maximum length
    longest_fragment = max(fragments, key=len)
    return longest_fragment


# ==============================================================================
# STAGE 2: THE SUPPLY LINE (File Paths)
# ==============================================================================

input_file = "data/fasta/gene.fna"
output_file = "data/raw/six_frame_summary.tsv"


# ==============================================================================
# STAGE 3: THE PIPELINE EXECUTION (Pure Linear Execution)
# ==============================================================================

print("=" * 75)
print("             WEEK 4 DAY 5: 6-FRAME TRANSLATION & TSV EXPORTER")
print("=" * 75)

# Step 1: Load Forward Sequence
print(f"\n[Step 1] Loading FASTA dataset from: {input_file}")
records = parse_fasta(input_file)
seq_id = list(records.keys())[0]
forward_seq = records[seq_id]
total_len = len(forward_seq)
gc_content = calculate_gc(forward_seq)

print(f" -> Locus ID:    {seq_id}")
print(f" -> Length:      {total_len:,} bp")
print(f" -> GC Content:  {gc_content}%")

# Step 2: Generate Reverse Complement Strand
print("\n[Step 2] Generating Reverse Complement (Anti-parallel Strand)...")
reverse_seq = get_reverse_complement(forward_seq)
print(f" -> Reverse Strand generated ({len(reverse_seq):,} bp)")

# Step 3: Define the 6 Reading Frames
# We package the 6 frames into a list of dictionaries so we can loop over them cleanly!
frames_to_process = [
    {"name": "Frame +1", "strand": "Forward (+)", "seq": forward_seq, "offset": 0},
    {"name": "Frame +2", "strand": "Forward (+)", "seq": forward_seq, "offset": 1},
    {"name": "Frame +3", "strand": "Forward (+)", "seq": forward_seq, "offset": 2},
    {"name": "Frame -1", "strand": "Reverse (-)", "seq": reverse_seq, "offset": 0},
    {"name": "Frame -2", "strand": "Reverse (-)", "seq": reverse_seq, "offset": 1},
    {"name": "Frame -3", "strand": "Reverse (-)", "seq": reverse_seq, "offset": 2},
]

# Step 4: Process and Translate all 6 Frames
print("\n[Step 3] Translating and analyzing all 6 reading frames...")
results = []

for frame in frames_to_process:
    # Translate this specific frame
    protein = translate_frame(frame["seq"], frame["offset"])

    # Count stop codons in this frame
    stop_count = protein.count("*")

    # Find the longest uninterrupted peptide piece
    longest_pep = get_longest_peptide(protein)

    # Store findings
    summary_record = {
        "frame_name": frame["name"],
        "strand": frame["strand"],
        "offset": frame["offset"],
        "total_aa": len(protein),
        "stop_codons": stop_count,
        "longest_pep_len": len(longest_pep),
        "longest_pep_seq": longest_pep
    }
    results.append(summary_record)

# Step 5: Print Summary Table to Terminal
print("\n" + "-" * 75)
print(f"{'Frame':<10} {'Strand':<14} {'Total AA':<10} {'Stops (*)':<10} {'Longest Peptide':<15}")
print("-" * 75)
for r in results:
    print(f"{r['frame_name']:<10} {r['strand']:<14} {r['total_aa']:<10} {r['stop_codons']:<10} {r['longest_pep_len']:<15}")
print("-" * 75)

# Step 6: Identify the Overall Champion Frame across the entire locus
champion = max(results, key=lambda x: x["longest_pep_len"])
print(f"\n>>> OVERALL CHAMPION: {champion['frame_name']} ({champion['strand']})")
print(f"    Longest uninterrupted peptide: {champion['longest_pep_len']} amino acids!")
print(f"    First 25 residues: {champion['longest_pep_seq'][:25]}...")

# Step 7: Export to TSV File (Tab-Separated Values)
print(f"\n[Step 4] Writing TSV report to: {output_file}")
with open(output_file, "w") as out_f:
    # Header row separated by \t and ended with \n
    header = "Frame\tStrand\tOffset\tTotal_AAs\tStop_Codons\tLongest_Peptide_Length\tFirst_25_AAs\n"
    out_f.write(header)

    # Each frame's data row
    for r in results:
        row = f"{r['frame_name']}\t{r['strand']}\t{r['offset']}\t{r['total_aa']}\t{r['stop_codons']}\t{r['longest_pep_len']}\t{r['longest_pep_seq'][:25]}\n"
        out_f.write(row)

print(f" -> Successfully saved TSV table to {output_file}!")
print("\n" + "=" * 75)
print("      WEEK 4 DAY 5 COMPLETE")
print("=" * 75)