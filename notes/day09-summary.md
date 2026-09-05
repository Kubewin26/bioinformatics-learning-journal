# 📌 Git Core Essentials & Command Reference

> **The Fundamental Rule of Git:**  
> Editing a file is not enough! Saving in Git is a 2-step process:  
> **1. Stage changes** (`git add`) ➔ **2. Snapshot changes** (`git commit`)

---

## 🛠️ Core Command Cheat Sheet

| Command | Action / Purpose | Pro-Tip |
| :--- | :--- | :--- |
| `git init` | Initializes a new Git repository in the current folder. | Creates hidden `.git` folder. **Do NOT delete it!** |
| `git status` | Shows the state of your working directory & staging area. | **Run constantly!** Before & after `git add`, before `git commit`. |
| `git add <file>` | Stages changes (moves them to the drafting table). | Use `git add <dir>` to stage all files inside a folder. |
| `git commit -m "msg"` | Permanently saves a snapshot of staged changes into `.git`. | Write messages to complete: *"If applied, this commit will..."* |
| `git diff` | Shows unstaged changes before you add them. | Use `--staged` to view staged changes; `--color-words` for word diffs. |
| `git log` | Displays commit history in reverse chronological order. | Combine with `--oneline --graph` or limit results with `-N` (e.g., `-5`). |

---

## 🔍 Detailed Breakdown & Best Practices

### 1. Repository Setup (`git init`)
* `git init` creates a hidden `.git` folder. This folder stores your entire project history.
* **Nested Repositories:** Never run `git init` inside an existing Git repository. One `git init` automatically tracks all subdirectories and files recursively.
* **Warning:** Deleting the `.git` folder deletes your entire project history!

### 2. Project Navigation (`git status`)
* `git status` is your compass. It tells you where you are, what files are modified, what is staged, and what is untracked.
* **Habit:** Run `git status` constantly:
  - Before `git add`
  - After `git add`
  - Before `git commit`

### 3. Staging & Committing (`git add` & `git commit`)
* `git add` moves files to the Staging Area.
* `git commit` writes the staged files into the `.git` vault as a permanent revision.
* **Writing Good Commit Messages:**
  - Keep the title brief (< 50 characters).
  - Use the imperative mood (e.g., *"Add README and Linux notes"* instead of *"Added notes"*).
  - A good commit message completes the sentence: **"If applied, this commit will [your message]."**

### 4. Reviewing Changes (`git diff`)
Always inspect your changes before saving:
* `git diff`: Shows what changed in your working directory compared to the last commit.
* `git diff --staged`: Compares your staged files against the last commit.
* `git diff --color-words`: Highlights exact word-level changes rather than full line changes.

### 5. Navigating History (`git log` & Pager Controls)
When repository history grows, `git log` uses a terminal **pager** (indicated by a `:` prompt at the bottom):
* **Spacebar**: Move to the next page.
* **`/word` + `Enter`**: Search for `word` in log messages (press `N` for next match).
* **`q`**: Quit the log viewer and return to the terminal.

#### Useful Log Options:
* `git log -5`: Shows only the last 5 commits.
* `git log --oneline`: Displays a compact, single-line summary of commits.
* `git log --oneline --graph`: Visualizes branch structures and commit references (`HEAD`, `main`).

### 6. Directories & Empty Folders (`.gitkeep`)
* **Git tracks files, not empty folders.** Git will ignore an empty directory.
* **Convention:** To track an empty directory, place an empty file named `.gitkeep` inside it (e.g., `touch results/.gitkeep`).

---