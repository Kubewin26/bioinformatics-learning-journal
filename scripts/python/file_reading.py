# file_reading.py
# Reading biological sequence files
# Winner Kubeyinje — Week 3, Day 5

# Open and read the sequences file line by line
print("=== Reading sequences from file ===")

with open("data/raw/sequences.txt", "r") as f:
    for line in f:
        line = line.strip()        # remove hidden newline characters (\n)
        if line:                   # skip empty lines (avoid division by zero!)
            gc = (line.count("G") + line.count("C")) / len(line) * 100
            print(f"Sequence: {line[:10]}... | Length: {len(line)} | GC: {gc:.1f}%")

# --- Writing results to a file ---
print("\n=== Writing results to file ===")

with open("data/raw/gc_results.txt", "w") as out:
    out.write("sequence\tlength\tgc_content\n")  # Write the table header
    
    with open("data/raw/sequences.txt", "r") as f:
        for line in f:
            line = line.strip()        # remove hidden \n
            if line:                   # skip empty lines
                gc = (line.count("G") + line.count("C")) / len(line) * 100
                # Write tab-separated columns with a newline at the end
                out.write(f"{line}\t{len(line)}\t{gc:.1f}\n")

print("Results written to data/raw/gc_results.txt")