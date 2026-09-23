# Python Syntax Quick Reference

## Winner Kubeyinje — Built during Week 3-4

### Functions

def function_name(parameter):
return result

### Loops

for item in list:
print(f"{item}: {len(item)}")

### File reading

with open("file.txt", "r") as f:
for line in f:
line = line.strip()
if line: # process line

### File writing

with open("output.txt", "w") as out:
out.write(f"{value}\t{other}\n")

### GC content

gc = (seq.count("G") + seq.count("C")) / len(seq) \* 100

### String slicing

seq[start:end] # end is excluded
seq[:10] # first 10 bases
seq[6:12] # bases at positions 6,7,8,9,10,11

### File modes

"r" = read only
"w" = write (DANGER: overwrites existing file)
"a" = append (adds to end, safe)

### .strip()

line = line.strip() # removes \n and whitespace from both ends

### Dictionaries

my_dict = {"key1": "value1", "key2": "value2"}
my_dict["key1"] # lookup: returns "value1"
my_dict.keys() # all keys
my_dict.values() # all values
my_dict.items() # all key-value pairs for looping

# Frequency counter pattern

if key in dict:
dict[key] += 1
else:
dict[key] = 1

### String reversal

seq[::-1] # reverses the entire string
comp[::-1] # reverse complement (after complementing)

### The 5-Stage Mental Model for Writing Scripts (The Kitchen Recipe)

When given any bioinformatics problem, organize your thoughts and script into 5 stages:

1. **Stage 1 (Tools)**: Define custom functions (`def`) to do specific small calculations (e.g., `calculate_gc()`).
2. **Stage 2 (Prep)**: Define file paths and empty collection containers (`input_file`, `output_file`, `results = {}`).
3. **Stage 3 (Open / Stove)**: Open file(s) with `with open(...) as f:` to stream lines without crashing RAM.
4. **Stage 4 (Inspect / Cooking)**: Loop with `for line in f:`, clean with `.strip()`, make decisions with `if/elif/else`, and use your Stage 1 tools.
5. **Stage 5 (Serve / Plating)**: Write results out to a file (`out.write()`) or print a summary table to the screen.

### String Methods for Parsing

line.startswith(">") # checks if line begins with a specific character/string
line[1:] # slices off the first character (skips '>')
line.split() # splits string by whitespace into a list of words
line.split()[0] # grabs the first word (useful for isolating sequence IDs)

### Multi-line Sequence Concatenation

current_seq = current_seq + line # joins multiple lines of sequence into one unbroken string
