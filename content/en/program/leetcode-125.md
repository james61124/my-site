---
title: "[ Leetcode 125 ] Valid Palindrome | Solution Approach & Explanation"
date: 2025-02-15
draft: false
author: "James"
tags:
  - Two Pointer
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

This problem requires determining whether a given string is a palindrome, ignoring case and non-alphanumeric characters.

Link🔗：[https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)

### **Solution - Opposite Direction Two Pointers**

This problem can be solved using an opposite direction two-pointer approach. The idea is to check whether the characters at the left and right pointers are the same. If they are, both pointers move inward. The main points to consider are ensuring that left and right do not go out of bounds and using isalnum() to check whether a character is alphanumeric.

**Time Complexity** - O( n ), as each element is checked at most once by either left or right.

**Space Complexity** - O( 1 ), since only two pointers are used.

#### **Implementation**

```cpp
bool isPalindrome(string s) {
    int left = 0;
    int right = s.size()-1;
    while(left < right) {
        while(left < right && !isalnum(s[left])) left++;
        while(left < right && !isalnum(s[right])) right--;
        if(tolower(s[left])!=tolower(s[right])) return false;
        left++;
        right--;
    }
    return true;
}
```