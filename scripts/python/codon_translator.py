# codon_translator.py
# Translates DNA sequences from FASTA files into amino acid peptides
# Winner Kubeyinje — Week 4, Day 3

# --- STAGE 1: TOOLS (The 64-Codon Genetic Code Dictionary) ---

CODON_TABLE = {
    # Phenylalanine & Leucine
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    # Leucine
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    # Isoleucine & Methionine (Start)
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    # Valine
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    # Serine
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    # Proline
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Threonine
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    # Alanine
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Tyrosine & Stop Codons
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    # Histidine & Glutamine
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    # Asparagine & Lysine
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    # Aspartate & Glutamate
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    # Cysteine, Stop, & Tryptophan
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    # Arginine
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    # Serine & Arginine
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    # Glycine
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def translate_dna(sequence):
    """
    Translates a DNA sequence in reading frame 1 into a protein sequence.
    Stops at the first Stop codon (*), or translates full sequence if desired.
    """
    protein = ""
    # Ensure uppercase
    sequence = sequence.upper()
    
    # Step through sequence in triplets (codons)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i : i + 3]
        amino_acid = CODON_TABLE.get(codon, "X")  # 'X' for unknown/ambiguous
        protein += amino_acid
        
    return protein

def parse_fasta(filepath):
    """Parses a multi-line FASTA file into a dictionary of {id: sequence}."""
    sequences = {}
    current_id = None
    current_seq = ""

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = current_seq
                current_id = line[1:].split()[0]
                current_seq = ""
            else:
                current_seq += line

        if current_id is not None:
            sequences[current_id] = current_seq

    return sequences


# --- STAGE 2: PREP & STAGE 3: OPEN / STREAM ---
fasta_input = "data/fasta/gene.fna"
output_file = "data/raw/translated_peptides.txt"

print("=== Running Codon Translation Engine on Teesside Dataset ===")
print(f"Reading from: {fasta_input}")
print(f"Writing to:   {output_file}\n")

gene_dict = parse_fasta(fasta_input)

# --- STAGE 4 & 5: TRANSLATE, SERVE & SAVE ---
with open(output_file, "w") as out:
    out.write("gene_id\tdna_length_bp\tprotein_length_aa\tfirst_10_aa\tfull_protein\n")
    
    for gene_id, dna_seq in gene_dict.items():
        protein_seq = translate_dna(dna_seq)
        dna_len = len(dna_seq)
        prot_len = len(protein_seq)
        preview_aa = protein_seq[:10]
        
        # Save to file
        out.write(f"{gene_id}\t{dna_len}\t{prot_len}\t{preview_aa}\t{protein_seq}\n")
        
        # Print summary to terminal
        print(f"Gene ID:           {gene_id}")
        print(f"DNA Length:        {dna_len} bp")
        print(f"Translated Protein: {prot_len} amino acids")
        print(f"First 10 Residues: {preview_aa}...")
        print(f"Total Stop Codons: {protein_seq.count('*')}")
        print("-" * 55)

print(f"\nTranslation complete! Report saved to {output_file}")