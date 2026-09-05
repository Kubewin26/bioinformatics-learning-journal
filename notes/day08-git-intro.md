# Day 8 — Git Introduction and Configuration

Date: July 20, 2026

## What Git Is

Git is a version control system. It tracks changes to files over time so I can still have and go back to the original document later if need be.

## The Three-Tree Architecture

Working Directory → Staging Area → Repository

- Working Directory: where I edit files on my computer right now. 
  That is the current working directory I am carrying out a project in.
- Staging Area (Index): where I collect changes I am ready to commit
  (like preparing samples before putting them in the freezer). 
  A temporary storage of some sort before the files are moved into the main storage location.
- Repository: where Git permanently stores my snapshots as commits. The main storage folder on GitHub. 

## Why This Matters For Bioinformatics

When I am running a pipeline on 200 samples and something breaks, Git lets me go back to the last working version. It also lets me share exactly what I did and when I did it — which is what reproducible science requires.

## Commands I Ran Today

- git --version        → confirmed git version 2.43.0
- git config --global user.name
- git config --global user.email
- git config --global core.editor "code --wait"
- git config --global init.defaultBranch main
- git config --list --global   → verified identity is set

## My Git Identity Is Now Set

Name: Winner Kubeyinje
Email: winner4medicine@gmail.com
Editor: VS Code
Default branch: main

## What I Learned Overall
- Version control is like an unlimited ‘undo’.
- Version control also allows many people to work in parallel.
- On a command line, Git commands are written as git verb options, where verb is what we actually want to do and options is additional optional information which may be needed for the verb.