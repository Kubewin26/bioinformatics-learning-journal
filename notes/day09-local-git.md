# Day 9 — Local Git: Init, Add, Commit

Date: July 21, 2026

## What I Did Today

- Created bioinformatics-learning-journal as a local Git repository
- Ran git init to initialise the repo
- Created README.md and wrote my 6-month learning plan inside it
- Staged README.md with git add
- Made my first commit with git commit -m
- Checked my commit history with git log --oneline

## The Three Commands I Will Use Every Day

git add <file>     → moves file to the staging area
git commit -m ""   → permanently snapshots staged changes
git status         → tells me exactly what state everything is in

## What git status shows at each stage

Before git add:     file appears red — untracked or modified
After git add:      file appears green — staged, ready to commit
After git commit:   nothing to commit — working tree clean

## Commit Message Rules I Am Learning

- Use the imperative mood: "Add README" not "Added README"
- Be specific: "Add DNA counter script" not "update"
- Keep it under 72 characters
- The message should complete the sentence: "This commit will..."

## What Surprised Me Today

[Write something here in your own words]

## Commands Practised

git init
git status
git add README.md
git commit -m "message"
git log --oneline