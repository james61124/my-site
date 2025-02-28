---
title: "[ Leetcode 873 ] Length of Longest Fibonacci Subsequence | 解題思路分享"
date: 2025-02-23
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

這題是 Two Sum 的變體，給定一個「遞增排序」的 array，要求找出兩個數，使它們的和等於目標值，並返回這兩個數的「1-based index」

題目連結🔗：[https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

### **解題思路 - DP + Hash Table**

這題可以透過 Single-Sequence Linear DP 來解，但與一般的 1D DP 不太一樣，因為我們的狀態轉移需要依賴兩個數字作為 subsequence 的結尾，因此我們需要使用二維 DP（2D DP） 來儲存狀態。

#### 狀態定義

我們使用一個 dp[j][i] 來表示以 arr[j] 和 arr[i] 結尾的最長 Fibonacci subsequence 的長度。對於每一個數 arr[i]，我們檢查他前面的每一個數 arr[j]，如果存在一個 k 使得 arr[i]+arr[j] = arr[k]，就表示 dp[i][k] = dp[i][j] + 1，此時更新 dp[i][k] = dp[i][j] + 1


首先我們需要一個 dp[i][j] 來表示以 arr[i], arr[j] 結尾時的 Length of Longest Fibonacci Subsequence，再來用 n^2 遍歷過每一個 i, j 的組合，如果我們可以在 arr 裡找到一個 index k 使得 arr[i]+arr[j] = arr[k]，就表示 dp[j][k] 要嘛是原本的數字，要嘛是 dp[i][j]+1，取大的那個紀錄

至於要如何在 arr 裡找到這樣子的 k，我們可以先用 unordered_map 把所有 value 都存下來，這樣可以直接用 count 來查找，就會快很多

**Time Complexity** - O( n )，每個元素最多被 right 或 left 掃過。

**Space Complexity** - O( 1 )，只使用了兩個指針

#### **Implementation**

```cpp
int lenLongestFibSubseq(vector<int>& arr) {
    vector<vector<int>>dp(arr.size(), vector<int>(arr.size(), 2));
    unordered_map<int, int>mp;
    int ans = 0;

    for(int i=0; i<arr.size(); i++) {
        mp[arr[i]] = i;
    }

    for(int i=1; i<arr.size(); i++){
        for(int j=0; j<i; j++){
            if(mp.count(arr[j]+arr[i])>0) {
                int k = mp[arr[j]+arr[i]];
                dp[i][k] = max(dp[j][i]+1, dp[i][k]);
                ans = max(ans, dp[i][k]);
            }
        }
    }

    return ans;
}
```