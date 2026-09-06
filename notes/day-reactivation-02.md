# Git Refresher, Branching & The Three-Area Architecture

**Date:** September 6, 2026  
**Focus:** Re-grounding Git fundamentals, practicing branching (`reactivation-branch`), and pushing to GitHub.

---

## 🧠 What I Revised Today

### 1. What Git Actually Is
Git is a version control system that acts like an indestructible digital lab notebook. Instead of saving multiple confusing file copies (like `script_v1.py`, `script_final.py`, `script_really_final.py`), Git tracks every single change to my files over time. It allows me to take snapshots of my work, review past changes, and safely roll back mistakes without losing data.

### 2. The Three-Area Architecture (How Git Thinks)
Saving work in Git is not a single click—it happens in three distinct zones:

1. **Working Directory (My Sandbox):**
   * This is where I actually create, view, and edit my files on my computer. Changes here are live but completely unprotected until saved.
2. **Staging Area / Index (The Drafting Table):**
   * When I finish editing, I use `git add` to place selected files into this middle zone. It allows me to choose exactly which changes I want to include in my next save, leaving out unwanted or temporary files.
3. **Repository (The Vault):**
   * When I run `git commit`, Git permanently locks the staged changes into the hidden `.git` folder as a snapshot with an ID and a message. Once a commit is made, that version is permanently recorded in project history.

### 3. Stepping Beyond `main`: Branching Workflows
Up until today, all my work had lived strictly on the primary `main` branch. Today, I took a major practical step forward by creating an isolated workspace branch:

* Created a separate branch called **`reactivation-branch`**.
* Used the modern **`git switch`** command to move my working environment over to this new branch.
* Safely added, committed, and pushed changes directly to `reactivation-branch` on GitHub without modifying or risking my `main` branch.

---

## 🛠️ Commands Practiced Today

| Command | What I Used It For Today |
| :--- | :--- |
| `git status` | Checked the pulse of my project—saw which files were modified, untracked, or staged. |
| `git diff` | Viewed the exact line-by-line changes in my files before staging them. |
| `git branch` | Listed existing branches and verified which branch I was on. |
| `git switch reactivation-branch` | Switched from `main` to my newly created `reactivation-branch`. |
| `git add` | Moved my updated files from the working directory to the staging area. |
| `git commit -m "..."` | Saved a permanent snapshot of my staged work on `reactivation-branch`. |
| `git log --oneline` | Checked my commit history in a clean, one-line summary view. |
| `git remote -v` | Verified where my local project connects on the cloud (GitHub). |
| `git push -u origin reactivation-branch` | Pushed my new branch and its commits directly up to GitHub. |

---

## 🔍 Concept Clarification: What Does `git remote -v` Do?

I was uncertain about what this command does, so here is the simple explanation:

* **`git remote`**: Tells Git, *"List the nicknames of the online servers linked to this folder."* (Usually, it just prints `origin`).
* **`-v` (Verbose / Detailed)**: Tells Git, *"Don't just show the nickname—show the full web address (URL)!"*
* **What the output means:**
  ```text
  origin  git@github.com:username/repo.git (fetch)
  origin  git@github.com:username/repo.git (push)
  ```
  It simply confirms the exact web address where Git will download (`fetch`) updates from, and where it will upload (`push`) my commits to on GitHub. Think of it as checking your phone's address book to make sure you have the right contact number before sending a message.

---

## 💭 Honest Reflection

A lot of Git still feels uncertain and slightly overwhelming, but completing this refresher session and successfully working on an independent branch gave my confidence a real boost after being away for over a month. 

I recognize that bioinformatics tools and version control cannot be mastered overnight or by passive reading. It requires repeated, iterative practice. By showing up daily, running warm-up drills, and writing commands until they become second nature, these tools will gradually move from my notes directly into my fingertips.