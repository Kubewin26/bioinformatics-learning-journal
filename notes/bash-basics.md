# Bash Basics Cheat Sheet

Date: July 17, 2026

## Navigation

| Command | Meaning | Example |
|---|---|---|
| pwd | Show current directory | pwd |
| ls | List files and folders | ls |
| ls -a | Show hidden files too | ls -a |
| ls -l | Show detailed list | ls -l |
| cd | Change directory | cd notes |
| cd .. | Move one level up | cd .. |
| cd ~ | Go to home directory | cd ~ |

## File And Folder Creation

| Command | Meaning | Example |
|---|---|---|
| mkdir | Create a folder | mkdir practice_files |
| touch | Create an empty file | touch notes/day05.md |
| nano | Edit a file in the terminal | nano notes/day05.md |

## File Inspection

| Command | Meaning | Example |
|---|---|---|
| cat | Print a small file | cat data/fake_dna.txt |
| less | Scroll through a file | less data/fake_dna.txt |
| head | Show first lines | head -n 2 data/fake_dna.txt |
| tail | Show last lines | tail -n 2 data/fake_dna.txt |
| wc | Count lines, words, characters | wc data/fake_dna.txt |
| wc -l | Count lines only | wc -l data/fake_dna.txt |
| wc -c | Count bytes/characters | wc -c data/fake_dna.txt |

## File Operations

| Command | Meaning | Example |
|---|---|---|
| cp | Copy a file | cp sample1.txt sample1_copy.txt |
| mv | Move or rename a file | mv old.txt new.txt |
| rm | Delete a file permanently | rm sample1.txt |

## Paths

| Symbol | Meaning | Example |
|---|---|---|
| ~ | My home directory | cd ~ |
| / | Root of the Linux filesystem | cd / |
| . | Current directory | ls . |
| .. | Parent directory | cd .. |

## Safety Notes

- `rm` permanently deletes files in Linux.
- Always run `pwd` before deleting files.
- Avoid `rm -r`, `rm *`, and `sudo rm` while still learning.
- Use `ls` to check what is inside a folder before changing or deleting anything.

## Commands I Have Seen But Not Mastered Yet

- grep
- find
- sed
- awk
- for loops
- shell scripts
- pipes
- redirects

I do not need to master these yet. They will return later during Bash for Genomics and real dataset analysis.