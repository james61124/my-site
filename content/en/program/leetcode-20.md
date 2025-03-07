---
title: "[ Leetcode 20 ] Valid Parentheses | Solution Approach & Explanation"
date: 2025-03-06
draft: false
author: "James"
tags:
  - String
  - Stack
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a string s containing only the characters (, ), {, }, [ and ], check whether the string forms a valid set of parentheses.

Link🔗：[https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

### **Problem Analysis**

This is a classic First In, Last Out (FILO) problem, which makes a stack the ideal data structure for solving it. We also need to consider edge cases carefully.

### **Solution - Stack**

We use a stack while iterating through the string:

- If we encounter a left parenthesis, we push it onto the stack.
- If we encounter a right parenthesis:
  - If the top of the stack is not the corresponding left parenthesis → invalid.
  - Otherwise, we pop the top element from the stack and continue iterating.

#### **How to Match Parentheses Efficiently?**

Using if-else statements to check pairs is possible, but it is inefficient and messy. A hash map is a more elegant solution.

#### **Avoid Stack Empty Access**

If we encounter a right parenthesis but the stack is empty, calling stack.top() would cause an error.
To prevent this, we simply return false immediately.

#### **Final Check**

Since the loop exits after iterating through the entire string, any remaining left parentheses would still be in the stack. Thus, to determine if the parentheses are valid, we just check if the stack is empty at the end.

**Time Complexity** - O( n ), since we iterate through the string once.

**Space Complexity** - O( n ), since we use a stack.

#### **Implementation**

```cpp
bool isValid(string s) {
    stack<char>st;
    unordered_map<char, char>mp = {{')', '('}, {'}', '{'}, {']', '['}};

    for(char c : s){
        if(mp.count(c)){
            if(st.empty() || mp[c] != st.top()) return false;
            else st.pop();
        } else st.push(c);
    }

    return st.empty();
}
```