# Day 3 - Inspecting Files

Date: July 15, 2026

Today I practiced inspecting text files using Bash.

Commands practiced:
- cat
- less
- head
- tail
- wc
- wc -l
- wc -c

Practice file:
data/fake_dna.txt

What I learned:
- cat prints a small file directly to the terminal.
- less opens a file in scroll/view mode.
- head shows the first lines of a file.
- tail shows the last lines of a file.
- wc counts lines, words, and characters.
- wc -l counts only lines.
- wc -c counts characters/bytes.

Why this matters in bioinformatics:
Bioinformatics files can be very large. 
Instead of opening huge files directly, I can inspect parts of them safely with head, tail, less, and wc.


Text editors - The most common is nano
Others include Emacs, Vim, Gedit and VScode (graphical editors). Notepad++ on Windows. 
mkdir -p - The -p option allows mkdir to create a directory with nested subdirectories in a single operation.
rm - removes files. rm by default only works on files, not directories. rm -r - removes directory
rm -i - asks for confirmation to delete a file. 
rm -r -i - for deleting directory with caution.
mv - renames files. mv is short for 'move'
mv -i (or mv --interactive) will cause mv to request confirmation before overwriting a file/directory name.
cp - copies a file instead of moving it.
cp -r - applies the command not just to the specified directory, but to all its contents.
When cp is given three or more arguments, the last argument must be a directory. 
cp copies the other files specified into that directory. If the last argument is a file name, you get an error.

Wildcards are special characters that can be used to represent unknown characters or sets of characters when navigating the Unix file system. 
* is a wildcard, which represents zero or more other characters. 
? is also a wildcard, but it represents exactly one character. 
