# Day 6 - Week 1 Mini-Project

Date: July 18, 2026

Today I used Bash commands to inspect and summarize a mock DNA dataset.

Input file:
data/fake_dna.txt

Commands used:
- cat
- head
- tail
- wc
- wc -l
- cp
- grep
- >

Files created:
- data/fake_dna_backup.txt
- results/first_two_samples.txt
- results/fake_dna_headers.txt
- results/fake_dna_line_count.txt

What I learned:
- I can use head to extract the first part of a file.
- I can use grep to find lines matching a pattern.
- I can use > to save command output into a file.
- FASTA-style headers begin with >.
- Counting headers can tell me how many sequence records are in a file.


‘grep’ is a contraction of ‘global/regular expression/print’. grep finds and prints lines in files that match a pattern.
To use it type grep, then the pattern we’re searching for and finally the name of the file (or files) we’re searching in.
By default, grep searches for a pattern in a case-sensitive way.
Give grep the -w option to limit matches to word boundaries. Like to get an exact word or pattern and not everything that contains the letters or patterns in them. Like The and Thesis, if you are looking for just "The". Note that a ‘word boundary’ includes the start and end of a line, so not just letters surrounded by spaces. 
To get a phrase and not just a word, use grep by putting the phrase in quotes.
Another useful option to use with "grep" is -n, which numbers the lines that match.
Use the option -v to invert our search, i.e., we want to output the lines that do not contain the word we are specifying.
We can add -r (recursive) to our grep command to search for a pattern through all the files in a directory and its subdirectories. 
Using wildcards, We use the -E option and put the pattern in quotes to prevent the shell from trying to interpret it. (If the pattern contained a *, for example, the shell would try to expand it before running grep.) The ^ in the pattern anchors the match to the start of the line. The . matches a single character (just like ? in the shell),


Mini-project summary:
The file data/fake_dna.txt contains 3 sequence records and 6 lines total.

# 🔍 Pattern Searching with `grep`

A practical reference guide for searching text and matching patterns using `grep` in the Unix/Linux shell.

---

## 📌 What is `grep`?

* **Origin:** Contraction of **g**lobal / **r**egular **e**xpression / **p**rint.
* **Function:** Searches through files line by line and prints lines that match a specified pattern.
* **Basic Syntax:**
  ```bash
  grep [options] "pattern" filename
  ```
* **Default Behavior:** Case-sensitive matching.

---

## 📊 Quick Options Table

| Option / Flag | Purpose | Example |
| :--- | :--- | :--- |
| *(none)* | Standard pattern search (case-sensitive) | `grep "ATG" sequence.fasta` |
| `-w` | Match **exact whole words** (word boundaries) | `grep -w "The" notes.txt` |
| `-n` | Prefix matching lines with their **line numbers** | `grep -n "error" log.txt` |
| `-v` | **Invert search** (print lines that do NOT match) | `grep -v "^#" config.txt` |
| `-r` | **Recursive search** through directories and subdirectories | `grep -r "sample_01" ./data/` |
| `-E` | Use **Extended Regular Expressions** (regex engine) | `grep -E "^>chr" genome.fa` |

---

## 🛠️ Key Options & Best Practices

### 1. Exact Word Boundaries (`-w`)
Prevents partial matches inside larger words.
* Without `-w`, searching for `The` also matches `Thesis`, `Together`, or `Other`.
* With `-w`, only the standalone word `The` matches.
* *Note:* Word boundaries include spaces, punctuation, and the start/end of a line.

### 2. Searching Phrases
Always enclose multi-word phrases in quotes so the shell treats them as a single search argument:
```bash
grep "DNA polymerase" notes.txt
```

### 3. Displaying Line Numbers (`-n`)
Shows the file line number alongside every match, making it easy to find locations in large scripts or data files:
```bash
grep -n "TODO" script.py
```

### 4. Inverting Matches (`-v`)
Outputs only the lines that **do not** contain the specified pattern. Commonly used to filter out comments or headers:
```bash
# Example: Print lines that do not contain 'Unclassified'
grep -v "Unclassified" taxonomy.tsv
```

### 5. Recursive Directory Search (`-r`)
Searches through all files inside the specified folder and all its subfolders:
```bash
grep -r "BRCA1" ./annotations/
```

---

## 🧬 Pattern Matching & Regular Expressions (`-E`)

When using special pattern characters, use the **`-E`** flag and **always enclose patterns in quotes** to prevent the shell from trying to expand wildcards (like `*` or `?`) before `grep` runs:

* **`^` (Caret):** Anchors the search to the **start of the line**.
  ```bash
  # Matches only lines starting with '>' (e.g., FASTA headers)
  grep -E "^>" sequences.fasta
  ```
* **`.` (Dot):** Matches **any single character** (equivalent to `?` in filename globbing).
  ```bash
  # Matches 'cat', 'cot', 'c1t', etc.
  grep -E "c.t" text.txt
  ```
