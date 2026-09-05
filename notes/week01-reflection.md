# Week 1 Reflection - WSL and Bash Basics

Date: July 19, 2026

## What I Practiced This Week

This week I learned the basics of working in WSL Ubuntu using the Bash/Unix command line.

I created my main bioinformatics learning workspace:

/home/hswkbioinfo/bioinformatics-roadmap

Main folders:
- data
- notes
- practice_files
- results
- scripts

## Concepts I Learned

### WSL
WSL means Windows Subsystem for Linux. It allows me to run Ubuntu/Linux on my Windows computer.

### Bash
Bash is the command language I use inside Ubuntu to interact with files, folders, programs, and future bioinformatics tools.

### Shell
The shell is the program that receives my typed commands and tells the operating system what to do.

### Directory
A directory is a folder.

### File Path
A file path is the address/location of a file or folder.

Example absolute path:
/home/hswkbioinfo/bioinformatics-roadmap/data/fake_dna.txt

Example relative path:
data/fake_dna.txt

### Absolute Path
An absolute path starts from the root directory `/`.

### Relative Path
A relative path starts from my current working directory.

## Commands I Practiced

| Command | What it does |
|---|---|
| pwd | Shows my current location |
| ls | Lists files and folders |
| ls -a | Lists hidden files too |
| ls -l | Shows detailed file information |
| cd | Changes directory |
| cd .. | Moves one level up |
| cd ~ | Goes to my home directory |
| mkdir | Creates a folder |
| touch | Creates an empty file |
| nano | Edits a file in the terminal |
| cat | Prints a small file |
| less | Opens a file for scrolling |
| head | Shows the first lines of a file |
| tail | Shows the last lines of a file |
| wc | Counts lines, words, and characters |
| cp | Copies files |
| mv | Moves or renames files |
| rm | Deletes files permanently |
| grep | Finds matching text patterns |
| > | Saves command output into a file |

## Mini-Project Summary

I created a mock DNA dataset:

data/fake_dna.txt

I used Bash to:
- inspect the file
- count lines
- extract the first two samples
- find FASTA-style headers
- save outputs into the results folder

Mini-project outputs:
- results/first_two_samples.txt
- results/fake_dna_headers.txt
- results/fake_dna_line_count.txt

## Commands I Understand Well

- pwd, cd, ls, mkdir, touch, nano, cp, mv, head, tail, less, cat, rm
I still need to practice all of them very well and repetitively.

## Commands I Still Need To Practise

- grep
- uniq
- wildcards * and ?


## Biggest Lesson From Week 1

I don't need to master all the bash commands immediately. I need to learn them slowly, iteratively repeatedly through practice. 

## How This Connects To Bioinformatics

Bioinformatics often involves large text-based biological data files such as FASTA, FASTQ, SAM/BAM summaries, VCF, and tabular data. Learning Bash helps me inspect, move, organize, and summarize these files before using specialised bioinformatics tools.
