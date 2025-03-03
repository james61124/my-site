---
title: "[ Leetcode 3 ] Longest Substring Without Repeating Characters | Solution Approach & Explanation"
date: 2025-03-03
draft: false
author: "James"
tags:
  - Array
  - Sliding Window
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a string **s**, find the length of the longest substring without repeating characters.

Link🔗：[https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### **Problem Analysis**

The objective is to find the longest substring without repeating characters, meaning we must examine every possible substring.

### **Brute Force**

The most straightforward brute-force approach is to enumerate all possible substrings and check for repeated characters. However, this results in a time complexity of O(n²), which is too slow and will cause time limit exceeded (TLE) errors. Therefore, we need a more optimized approach.

### **Solution - Variable Length Sliding Window**

Using the Sliding Window technique, we can avoid checking unnecessary substrings. We start with left = 0, right = 0, and expand right first. When we encounter repeated characters, we move left forward accordingly. However, this raises two key questions:

1. How do we determine if a character is repeated?
2. How should we move left forward?

#### **How to Detect Repeated Characters?**

As right moves forward, we can store encountered characters in a hash table, which allows for O(1) lookup time. We can use either an unordered_map or an unordered_set, depending on further requirements.

#### **How to Move left Forward?**

A basic approach is to store encountered characters in an unordered_set. Whenever right encounters a repeated character, left moves forward one step at a time, removing characters from the set until the repeated character is no longer present in the window. Then, right continues expanding. However, this method requires a while loop that may iterate over nearly the entire string, making it inefficient.

A more optimal approach is to store the index of each character in an unordered_map. When right encounters a repeated character, we can instantly retrieve its last seen index. At this point, left has two options:

- If the stored index is less than left, it means the character is no longer in the sliding window, so left remains unchanged.
- Otherwise, update left to index + 1 to shrink the window efficiently.

This method eliminates the need to erase characters from a set and avoids unnecessary while loops.

**Time Complexity** - O( n ), as each element is visited at most twice (once by right, once by left).

**Space Complexity** - O(min(n,m))- O(min(n, m)), where n is the string length and m = 26 (since we are only dealing with English letters).

#### **Implementation**

```cpp
int lengthOfLongestSubstring(string s) {
    int left = 0;
    int right = 0;
    int result = 0;
    unordered_map<char, int>umap;

    while(right<s.size()){
        if(umap.count(s[right])>0){
            left = max(left, umap[s[right]]+1);
        }
        umap[s[right]] = right;
        result = max(result, right-left+1);
        right++;
    }
    return result;
}
```