# Week 3, Day 3: Decision Making, Conditionals, and Biological Classification

**Date:** September 14, 2026  
**Author:** Winner Kubeyinje  
**Topic:** Boolean Logic, Conditional Architecture, and the Return vs. Print Paradigm

---

## 1. Objectives Completed Today

- Learned Python decision-making using `if`, `elif`, and `else` blocks.
- Learned the critical distinction between assignment (`=`) and comparison (`==`).
- Clarified the fundamental difference between `return` (returning data to memory) and `print()` (displaying pixels to human eyes).
- Built and tested two biological classification functions in `scripts/python/conditionals.py`:
  1. `classify_gc()`: Categorizes sequences into High, Low, or Normal GC content.
  2. `classify_length()`: Categorizes sequences into Short (primers/probes), Medium (fragments), or Long (genes/chromosomal regions).
- Discovered string repetition using the `*` operator (e.g., `"ATCG" * 130` = 520 bp).
- Traced the flow of execution mentally and predicted all outputs with 100% accuracy before running the code.

---

## 2. Core Concepts & Technical Mechanics

### Assignment (`=`) vs. Comparison (`==`)

- **`=` (Assignment Operator)**: Takes the value on the right and stores it into the variable container on the left (`dna = "ATCG"`).
- **`==` (Comparison Operator)**: Asks Python a question: _"Are these two values identical?"_ Evaluates strictly to a boolean (`True` or `False`).

### Anatomy of a Conditional Ladder: Why One `if`, Many `elif`s, One `else`

- **`if` (Exactly ONE)**: Opens the decision tree. It is the initial entrance gate. If you write another `if`, you start a brand-new, independent decision tree.
- **`elif` (As many as needed: 0, 1, 10, etc.)**: Short for _"else if"_. Only checked if all preceding checks evaluated to `False`. Allows multiple alternative branches within the same decision tree.
- **`else` (At most ONE, at the end)**: The catch-all safety net. If every single `if` and `elif` above evaluated to `False`, the `else` block executes automatically.
- **Short-Circuit Execution**: Once any branch evaluates to `True`, its block executes, the function returns, and all remaining branches are skipped.

### The Great Distinction: `return` vs. `print()`

- **`print()` (For Human Eyes)**: Displays output onto the terminal screen. The computer cannot reuse or remember what was printed; it does not exist in memory after printing.
- **`return` (For Computer Memory)**: Hands the computed value back to whoever called the function. It allows the output of one function to be stored in a variable or fed directly into another function in an automated pipeline.
- _Analogy_: `print()` is shouting a test result out the window; `return` is handing the physical test report to the doctor to prescribe treatment.

### String Multiplication (`*`)

- In Python, multiplying a string by an integer repeats that string:
  ```python
  seq_long = "ATCG" * 130  # Generates 520 bases instantly
  ```
