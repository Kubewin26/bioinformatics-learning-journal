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
