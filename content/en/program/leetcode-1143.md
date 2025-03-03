---
title: "[ Leetcode 1143 ] Longest Common Subsequence | Solution Approach & Explanation"
date: 2025-03-01
draft: false
author: "James"
tags:
  - Dynamic Programming
  - String
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given two strings, text1 and text2, find the length of their Longest Common Subsequence (LCS).

⚠️ Note:

- A subsequence does not need to be contiguous but must maintain the original order.
- If there is no common subsequence, return 0.

Link🔗：[https://leetcode.com/problems/longest-common-subsequence/](https://leetcode.com/problems/longest-common-subsequence/)

### **Solution - DP (Double-Sequence Linear DP Problem)**

This problem can be solved using Double-Sequence Linear DP, as the input consists of two strings. We define dp[i+1][j+1] to represent the length of the longest common subsequence (LCS) ending at text1[i] and text2[j].

Initially, we set all values in dp to 0, since the LCS length for an empty string is 0. The following diagram illustrates this approach using text1 = "ace" and text2 = "abcde".

![DP](/images/program/leetcode-1143/DP-Table.JPEG)

By iterating through both strings using a nested loop, we apply the following rules:

**When characters match**: The LCS length increases by 1. Thus, dp[i+1][j+1] = dp[i][j] + 1.

**When characters do not match**: The LCS length remains the maximum of dp[i][j+1] and dp[i+1][j], meaning that adding a character does not increase the LCS length.

**Final answer**: The bottom-right cell of the dp table gives the final LCS length.

**Time Complexity** - O( m × n ), as we iterate over both strings.

**Space Complexity** - O( m × n ), due to the creation of a 2D array.

#### **Implementation**

```cpp
int longestCommonSubsequence(string text1, string text2) {
    vector<vector<int>>dp(text1.size()+1, vector<int>(text2.size()+1, 0));
    for(int i=0; i<text1.size(); i++){
        for(int j=0; j<text2.size(); j++){
            if(text1[i]==text2[j]){
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1);
            } else {
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }

    return dp[text1.size()][text2.size()];
}
```

### **Space Optimization**

The above approach constructs a full dp table. However, we only need the last two rows of the table at any given time, allowing us to optimize the space complexity to O(min(m, n)).

```cpp
int longestCommonSubsequence(string text1, string text2) {

    if (text1.size() < text2.size()) swap(text1, text2); 
    vector<int>prev(text2.size()+1, 0);
    vector<int>cur(text2.size()+1, 0);

    for(int i=0; i<text1.size(); i++){
        for(int j=0; j<text2.size(); j++){
            if(text1[i]==text2[j]){
                cur[j+1] = prev[j]+1;
            } else {
                cur[j+1] = max(prev[j+1], cur[j]);
            }
        }
        swap(prev, cur);
    }

    return prev[text2.size()];
}
```