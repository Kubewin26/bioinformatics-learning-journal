# Day 4 - Copying, Moving, Renaming, and Removing Files

Date: July 16, 2026

Today I practiced manipulating files and folders safely using Bash.

Commands practiced:
- mkdir
- touch
- cp
- mv
- rm
- ls
- ls -l

What I learned:
- cp copies files.
- mv can rename files.
- mv can also move files into another folder.
- rm permanently deletes files in Linux.
- ../ means the parent directory.
- I should be careful with rm because Linux does not use a recycle bin.

Examples:
cp sample1.txt sample1_copy.txt
mv sample3.txt renamed_sample3.txt
mv sample1_copy.txt ../data/
rm sample1.txt

Safety rule:
Only use rm when I am sure I am deleting the correct practice file.
Do not use rm -r, rm *, or sudo rm while learning unless I fully understand the command.



I also learned: 
wc is the ‘word count’ command: it counts the number of lines, words, and characters in files (returning the values in that order from left to right).
wc -l - shows only the number of lines per file.
The -m and -w options can also be used with the wc command to show only the number of characters or the number of words, respectively.
The greater than symbol, >, tells the shell to redirect the command’s output to a file instead of printing it to the screen.
The "cat" command gets its name from ‘concatenate’ i.e. join together, and it prints the contents of files one after another.
The command "less" displays a screenful of the file, and then stops. You can go forward one screenful by pressing the spacebar, or back one by pressing b. Press q to quit.
The "sort" command is used to sort the contents of a file.
The -n option specifies that the "sort" is numerical instead of alphanumerical. 
"head" is used to get the first few lines of a file. Using -n with head tells it the number of lines in the file we want to see; -n 20 would get the first 20, and so on. It prints lines from the start of a file.
The "echo" command is used to print strings.
The operator >>, unlike the >, appends output to that already present in a file. The > operator overwrites the previous output with the new one.
The "tail" prints lines from the end of a file.
The vertical bar, |, between two commands is called a pipe. It tells the shell that we want to use the output of the command on the left as the input to the command on the right. E.g. sort -n lengths.txt | head -n 1
The pipe character | is used to connect the output from one command to the input of another. > is used to redirect standard output to a file. 
The "cut" command is used to select or ‘cut out’ certain sections of each line in the file for further processing while leaving the original file unchanged.
"cut" expects the lines to be separated into columns by a Tab character. A character used in this way is called a delimiter. The -d option is used to specify the delimiter; the -f option is used to specify the field (column) we want to extract. 
The uniq command filters out adjacent matching lines in a file.

# 🐚 Bash Command-Line Utilities & Redirection

A reference guide for file inspection, text manipulation, and stream redirection in the Unix/Linux shell.

---

## 📊 Quick Reference Table

| Tool / Operator | Syntax / Flag | Primary Function | Example |
| :--- | :--- | :--- | :--- |
| `wc` | `-l`, `-w`, `-m` | Count lines, words, or characters | `wc -l sequences.txt` |
| `cat` | — | Concatenate and print entire file contents | `cat file1.txt file2.txt` |
| `less` | — | Paginated screen-by-screen file viewer | `less large_file.txt` |
| `head` | `-n <num>` | Print first *N* lines of a file | `head -n 20 data.txt` |
| `tail` | `-n <num>` | Print last *N* lines of a file | `tail -n 10 data.txt` |
| `echo` | — | Print strings/text to the terminal | `echo "Hello World"` |
| `sort` | `-n` | Sort lines (alphabetical by default; `-n` for numeric) | `sort -n lengths.txt` |
| `uniq` | — | Filter out **adjacent** duplicate lines | `sort file.txt \| uniq` |
| `cut` | `-d '<delim>' -f <col>` | Extract specific columns/fields | `cut -d ',' -f 1,3 data.csv` |
| `>` | — | Redirect standard output to a file (**overwrites**) | `head -n 5 in.txt > out.txt` |
| `>>` | — | Redirect standard output to a file (**appends**) | `echo "new line" >> out.txt` |
| `\|` | — | **Pipe**: Connect stdout of left command to stdin of right | `sort -n data.txt \| head -n 1` |

---

## 🔍 1. Inspecting File Contents

### `wc` (Word Count)
Counts lines, words, and characters (bytes) in files.
* Default output format (left to right): `[lines] [words] [characters] [filename]`
* **`-l`**: Count **lines** only.
* **`-w`**: Count **words** only.
* **`-m`**: Count **characters** only.

### `cat` (Concatenate)
Derived from *concatenate* (to link things together). Prints the entire content of one or more files to standard output sequentially.

### `less` (Paginated Viewer)
Displays file contents one screenful at a time without loading the whole file into memory.
* **`Spacebar`**: Scroll forward one screen.
* **`b`**: Scroll backward one screen.
* **`q`**: Exit viewer.

### `head` and `tail`
* **`head`**: Prints lines from the **start** of a file. Use `-n <num>` to specify line count (e.g., `head -n 20 file.txt`).
* **`tail`**: Prints lines from the **end** of a file. Use `-n <num>` to view the last *N* lines.

---

## ✂️ 2. Processing and Filtering Data

### `sort`
Sorts lines in a file.
* **Default:** Alphanumeric sorting (e.g., `1, 10, 2, 20`).
* **`-n`**: **Numeric sorting** (e.g., `1, 2, 10, 20`).

### `uniq`
Removes duplicate lines from input.
> ⚠️ **Important:** `uniq` only filters **adjacent** matching lines. To remove all duplicates across an entire file, always sort the file first:
> ```bash
> sort data.txt | uniq
> ```

### `cut` (Field Extractor)
Extracts specific sections/columns from each line of a file without modifying the original file.
* **Default delimiter:** Tab character (`\t`).
* **`-d`**: Specifies a custom delimiter (e.g., `-d ','` for CSV files).
* **`-f`**: Specifies the field/column number to extract (e.g., `-f 2` for column 2).

---

## 🔄 3. Pipes and Redirection

### Redirection Operators (`>` vs `>>`)
* **`>` (Overwrite):** Directs command output into a target file, completely replacing any existing content.
* **`>>` (Append):** Directs command output to the end of a file, preserving previous contents.

### Pipe (`|`)
Connects the **standard output** of the command on the left directly into the **standard input** of the command on the right.
```bash
# Example: Sort numbers in lengths.txt numerically, then grab the smallest single value
sort -n lengths.txt | head -n 1
```

