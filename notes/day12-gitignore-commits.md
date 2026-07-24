# Day 12: Git Ignore Rules & Commits Best Practices

**Date:** July 24, 2026  
**Topic:** Ignoring files with `.gitignore` and writing professional commit messages.

---

## 1. The `.gitignore` File

### ❓ Why We Need It in Bioinformatics
Bioinformatics pipelines constantly generate extremely large datasets, temporary log files, and intermediate outputs. We do **not** track these in Git because:
* **Large Files:** Raw sequencing reads (`.fastq`), alignments (`.sam`, `.bam`), and reference genomes (`.fasta`) are too large for GitHub (which has a strict file limit of 100MB, and a recommended repository size of 1GB–5GB).
* **Noise:** Tool logs, system caches, and intermediate scratch files clutter your history.

### ⚙️ How `.gitignore` Works
* It is a plain text file named **`.gitignore`** located in the root directory of your repository.
* Each line in the file contains a pattern of files/folders to ignore.
* Once committed and pushed, Git will completely ignore any files matching those patterns.

### 🔍 Wildcard (`*`) Syntax
* The asterisk (`*`) is a wildcard representing **zero or more characters**.
* E.g., `*.bam` tells Git: *"Ignore any file ending in `.bam`, regardless of what name comes before it."*

#### Common Bioinformatics `.gitignore` Patterns:
```text
# Ignore raw genomic/sequencing data
*.fastq
*.fastq.gz
*.fq
*.fq.gz
*.fasta
*.fa

# Ignore alignment files
*.sam
*.bam
*.bai

# Ignore system files and local configurations
.DS_Store
.venv/
node_modules/

## ✍️ 2. Anatomy of a Good Commit Message

Commit messages are a record of your professional history. Writing them well is essential for clean collaboration.

### 🔑 The Golden Rules of Commits:
* **Atomic Commits (Do One Thing):** Every commit should make **one** self-contained change. Do not bundle layout fixes, documentation updates, and bug fixes into a single commit.
* **Be Clear and Concise:** The title should state exactly what changed.
* **Use the Imperative Mood:** Start the message with a verb as if giving a command (e.g., `"Add gitignore rules"` instead of `"added gitignore rules"`).

### 💡 Example of Good vs. Bad Commits:
* ❌ **Bad:** `git commit -m "fixed stuff and added some fasta files and also formatted the readme"`
* 🟢 **Good:** `git commit -m "Add .gitignore to block large FASTQ/BAM files"`