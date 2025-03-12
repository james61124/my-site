---
title: "[ Leetcode 217 ] Contains Duplicate | Solution Approach & Explanation"
date: 2025-03-10
draft: false
author: "James"
tags:
  - Array
  - Hash Table
  - Easy
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given an integer array **nums**, determine if any value appears **at least twice**.

Link🔗: [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

---

### **Solution Approach - Hash Table**

The idea is straightforward: store each number in a **Hash Table** (using `unordered_set` in C++). If we encounter a number that already exists in the Hash Table, we return **true**.

Since checking for the existence of a number in a **Hash Table** is O(1) on average, this solution is efficient.

---

**Time Complexity** - O( n )
**Space Complexity** - O( n )

---

### **Implementation**

```cpp
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> uset;

    for (int& num : nums) {
        if (uset.count(num)) return true; 
        uset.insert(num);         
    }

    return false;
}
