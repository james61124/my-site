---
title: "[ Leetcode 1343 ] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold | Solution Approach & Explanation"
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

Given an integer array **nums**, along with two integers **k** and **threshold**, find the number of subarrays of length **k** whose average is greater than or equal to **threshold**.

Link🔗：[https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

### **Problem Analysis**

The goal is to find all subarrays of length k that meet the given condition. This means we need to examine every subarray of length k.

### **Brute Force**

A straightforward approach is to enumerate all possible subarrays of length k. However, for each subarray, we need another loop to compute its sum. Given an array of length N, this approach results in a time complexity of O(N * k), which is inefficient due to redundant calculations.

### **Solution - Fixed-Length Sliding Window**

Using the Fixed-Length Sliding Window technique eliminates redundant calculations. We maintain two pointers, left and right, to represent the current subarray. Instead of recalculating the sum for each subarray from scratch, we update it incrementally by subtracting the leftmost element and adding the new rightmost element.

**Time Complexity** - O( n ), since each element is processed at most once.

**Space Complexity** - O( 1 ), as only a few extra variables are used.

#### **Implementation**

```cpp
int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    int left = 0;
    int right = 0;
    int numOfSubarrays = 0;
    int sum = 0;
    int target = threshold*k;

    while(right<arr.size()){
        sum += arr[right];
        if(right-left+1 == k){
            if(sum >= target) numOfSubarrays++;
            sum -= arr[left];
            left++;
        }
        right++;
    }
    return numOfSubarrays;
}
```