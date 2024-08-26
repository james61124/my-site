---
title: "DP Series - The Rod Cutting Problem"
date: 2024-01-21
draft: false
author: "James"
tags:
  - Algorithm
  - Dynamic Programming
image: /images/program/Algorithm.png
description: ""
toc: 
categories:
  - Algorithm
---

---------------------------------------------------------------------------------------------

Given that selling a rod of length i yields a profit of p<sub>i</sub> , how do we cut a rod of length n to maximize the total revenue?

---------------------------------------------------------------------------------------------

### **Method 1: Recursion**
The most straightforward approach is to solve it using recursion. As shown in the figure below, r<sub>n</sub> represents the maximum revenue obtainable by cutting a rod of length n. Suppose i is the length of the first segment in the optimal solution; then <mark>r<sub>n</sub> = p<sub>i</sub> + r<sub>n−i</sub></mark>, because p<sub>i</sub> is the revenue from the first segment in the optimal solution, and adding the maximum revenue from the remaining part gives us the answer.

How do we find i? By looping through i from 0 to n−1, evaluating each combination <mark>p<sub>i</sub> + r<sub>n−i</sub></mark>, and selecting the maximum value as the answer.

However, this approach has a problem: each time we compute r<sub>n−i</sub>, it requires recursively calculating its optimal solution, leading to repeated calculations. For instance, when computing r<sub>4</sub>, we need to compute r<sub>3</sub>, r<sub>2</sub>, r<sub>1</sub>, r<sub>0</sub>, and computing r<sub>3</sub> requires recomputing r<sub>2</sub>, r<sub>1</sub>, r<sub>0</sub>. Therefore, we can use Dynamic Programming (DP) to save time.

![Recursive](/images/posts/the-rod-cutting-problem/Recursive.jpg)


### **Method 2: DP**

We can build a table to store the values of each r<sub>i</sub>, so we don’t have to recalculate them every time i is needed.

Given r<sub>0</sub> and r<sub>1</sub>, we can compute r<sub>2</sub> as follows: <mark>r<sub>2</sub> = max( p<sub>1</sub> + r<sub>1</sub>, p<sub>2</sub> + r<sub>0</sub> )</mark>. Next, using r<sub>1</sub> and r<sub>2</sub>, we can compute r<sub>3</sub>, and finally determine r<sub>5</sub>. The most crucial part is still the recursive formula <mark>p<sub>i</sub> + r<sub>n-i</sub></mark>.

![DP](/images/posts/the-rod-cutting-problem/DP.jpg)

### **Quick Note**
Building a table to store repetitive parts in recursion is a key technique in Dynamic Programming!