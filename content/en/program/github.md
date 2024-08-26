---
title: "Introduction to Github for Beginners"
date: 2024-01-18
draft: false
author: "James"
tags:
  - Github
image: /images/program/github.png
description: ""
toc: 
categories:
  - Github
---

## **What is Github？**
Git is a version control software, while Github is an online platform for storing code. It organizes projects into repositories, allowing users to use Git for version control and making collaboration within a team easier.

## **Why Use Github**

----------------------------------------------------------------------------------------------

In a project, I make changes to A, someone else modifies B, and I update C. Things can quickly get messy.

----------------------------------------------------------------------------------------------

1. It can store a large collection of your work portfolio.
2. It makes version control, branching, and tracking changes easy.
3. It’s free and open-source, allowing you to reference and learn from other developers’ code.

## **Prerequisites**
1. Install Git

## **Creating Your First Github Repository**
Go to Github, click on Your repositories, then click on New. Fill in the Repository name and create it. There are two ways to edit the empty repository you just created:

1. Create files in the repository and then clone it locally.
2. Directly upload your code to the repository.


## **Cloning to Your Local Machine**
Add any file in the repository, then return to your local environment. Open the terminal and type
```shell=1
git clone <repo-url>
```
You’ll see a new folder on your local machine. After making changes, you can upload the modified code back to the repository.

## **Uploading Code to the Repository**
If you didn’t clone the empty project, you can create a project (a folder) on your computer or use an existing one that you want to upload. Enter the terminal and navigate to this folder:
```shell=1
git init
git remote add origin <repo-url>
git add .
git commit -m "your_commit"
git push origin master
```
Here’s a brief explanation of each command:
1. <mark>git init</mark> Initializes a .git folder, which stores all version control information.
2. <mark>git remote add origin</mark> The Github repository is referred to as the remote repository. This command links your local folder to the remote repository so you can push your code.
3. <mark>git add .</mark> The . represents all files. It stages all files for the next commit.
4. <mark>git commit -m </mark> Adds a message to each commit. Replace your_commit with your commit message.
5. <mark>git push origin master</mark> Pushes your project to the repository, specifically to the master branch.

## **Introduction to Branches**
First, let’s understand what a branch is. Think of branches as parallel timelines. They can develop independently without affecting each other. Branches have three main uses:

1. During updates, you might want to keep a stable version of the old functionality while developing new features. You can create a new branch for this, ensuring the new feature doesn’t impact the main functionality.
2. For multi-person development, each person can manage their own branch and merge changes later, eliminating the need to copy and paste code.
3. In academic research, you might need to experiment with different changes to see their impact. Branches allow you to control different functionalities without commenting out old code to run new features.

It’s essential to distinguish between local and remote in Github. Any changes made locally won’t affect the remote repository until they’re pushed. Communication should be clear about whether we’re discussing local commits, local branches, remote commits, or remote branches.
```shell=1
git branch
```
```git branch``` shows which branches exist and which branch you’re currently on locally.
```shell=1
git checkout [-b] <branch-name>
```
```git checkout``` switches to another branch locally. Adding -b creates a new branch locally and switches to it.
```shell=1
git push origin <branch-name>
```
Finally, this command pushes the local branch information to the remote repository.

Image source: [Medium](https://miro.medium.com/v2/resize:fit:1400/1*mtsk3fQ_BRemFidhkel3dA.png)