# 📌 Markdown, Git History, Undoing Changes & SSH Remotes

> **Bioinformatics Best Practice:**  
> Keep your code files modular and small. This gives you precise control over what you stage, commit, or restore, preventing accidental damage to your project.

---

## 📝 1. Markdown Documentation Syntax
Markdown is the universal language of data science and bioinformatics documentation.

| Element | Markdown Syntax | Output Example |
| :--- | :--- | :--- |
| **Heading 1** | `# Title` | Title header |
| **Heading 2** | `## Subtitle` | Section header |
| **Bold** | `**text**` | **text** |
| **Italic** | `*text*` | *text* |
| **Inline Code** | `` `code` `` | `code` |
| **Code Block** | \`\`\`python <br> print("Hello") <br> \`\`\` | Fenced code block |
| **Link** | `[GitHub](https://github.com)` | [GitHub](https://github.com) |
| **Image** | `![alt text](image_url)` | Embedded image |
| **Lists** | `- item` or `1. item` | Bulleted or numbered list |

---

## 🕰️ 2. Git History & Commit Referencing

### The `HEAD` Pointer
* **`HEAD`** refers to the most recent commit in your current active branch.
* **`HEAD~1`** means the commit *before* the current one.
* **`HEAD~3`** goes back 3 commits from your current state.

### Reviewing Specific Changes
* `git diff HEAD`: Compares your current working directory to the most recent commit.
* `git diff HEAD~1`: Compares your working directory to the previous commit.
* `git show [commit_ID]`: Displays the commit message and the exact changes made in that specific commit (instead of comparing against the working directory).
* **Short Hashes:** You don't need to type the full 40-character commit hash. Using the first **7 characters** (e.g., `git show f22b25e`) is enough.

---

## ⎌ 3. Undoing & Reverting Changes

Git offers different tools depending on whether changes are staged or committed:

> [!WARNING]  
> When restoring a file to an older state, you must target the commit identifier **before** the unwanted changes were made.

### Uncommitted Changes
* **`git restore <file>`**: Discards unstaged modifications in your working directory, returning the file to the state of `HEAD`.
* **`git restore .`**: Discards unstaged changes in **all** files in your current directory.
* **`git restore -s [commit_ID] <file>`**: Restores a file to its state at a specific past commit (`-s` stands for source).

### Staged Changes
* **`git restore --staged <file>`**: Unstages a file (removes it from the staging area so you can safely edit or restore it).

### Committed Changes
* **`git revert [commit_ID]`**: Creates a **new commit** that reverses the exact changes of an erroneous commit. This keeps your commit history intact and is the safest way to undo shared changes.
* **`git checkout [commit_ID]`**: Temporarily takes your repository back to a past state to inspect it. 
  *(Remember to run `git checkout main` to return to your current work!)*

---

## 🔑 4. SSH & Remote Connections (`origin`)

### How SSH Cryptography Works (Key Pair)
* **Secure Shell Protocol (SSH)** uses a public/private key pair:
  * **Public Key (Padlock):** Copied and added to GitHub. It encrypts communication.
  * **Private Key (Key):** Kept secure on your WSL machine. Only this key can unlock access.
* **Security Rule:** Regularly check your registered SSH keys on GitHub to ensure there are no unauthorized keys.

### Remotes and Syncing
* **`origin`**: The default nickname Git uses to refer to your remote GitHub repository URL.
* **`git push`**: Copies your local commits to your remote GitHub repository.
* **`git pull`**: Downloads and merges changes from your remote GitHub repository to your local machine.

> [!TIP]  
> On GitHub, hovering your mouse over relative timestamps (e.g., *"3 hours ago"*) reveals the exact date and time the commit was created.