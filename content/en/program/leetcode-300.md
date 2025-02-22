---
title: "[ Leetcode 300 ] Longest Increasing Subsequence | Solution Approach & Explanation"
date: 2025-01-29
draft: false
author: "James"
tags:
  - Binary Search
  - Dynamic Programming
  - Greedy
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given an array, find the longest increasing subsequence (LIS). The elements in this subsequence must appear in increasing order but do not need to be consecutive in the original array.

Link🔗：[https://leetcode.com/problems/longest-increasing-subsequence/](https://leetcode.com/problems/longest-increasing-subsequence/)

### **Method 1 - Dynamic Programming**

**Time Complexity** - O( n^2 ), due to the nested loops.

**Space Complexity** - O( n ), as we need an array of size n for dp.

##### **Step 1**

Create a dp array where dp[i] represents the length of the LIS that ends at nums[i].

##### **Step 2**

Initially, every number is an increasing subsequence of length 1 by itself. Thus, set all dp[i] = 1.

##### **Step 3**

For each number nums[i], check all previous numbers nums[j] (where j < i):
- If nums[j] < nums[i], it means nums[i] can be appended to the LIS ending at nums[j].
- Update dp[i] = max(dp[i], dp[j] + 1), meaning if nums[i] can extend the LIS from nums[j], then its length will be dp[j] + 1. If dp[i] was already greater, we keep its value unchanged.

##### **Step 4**

The length of the LIS is the maximum value in the dp array.

#### **Implementation**

```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int>dp(n, 1);
    for(int i=1; i<n; i++) {
        for(int j=0; j<i; j++) {
            if(nums[i]>nums[j]){
                dp[i] = max(dp[j]+1, dp[i]);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}
```

### **Method 2 - Binary Search + Greedy**

**Time Complexity** - O( nlogn ), since we iterate over nums (O(n)) and use binary search (O(log n)).

**Space Complexity** - O( n ), as we maintain a tails array.

##### **Step 1**

Create a tails array, where tails[i] stores the smallest possible ending element of an increasing subsequence of length i+1.

##### **Step 2**

For each element in nums, use Binary Search to find the appropriate position in tails:
- If the number is greater than all elements in tails, append it to the end. This increases the length of tails, meaning the LIS length increases.
- Otherwise, find the first element in tails that is greater than or equal to the current number and replace it. This does not increase the LIS length, but it keeps tails minimized, leaving more room for future LIS extensions.

##### **Step 3**

At the end, the length of tails is the length of LIS. However, tails itself is not the LIS but rather a structure that helps track the smallest elements possible, ensuring that the LIS can be extended optimally.

##### **Example**

Consider nums = [1, 4, 8, 9, 5, 6, 7]. After processing index 3, tails = [1, 4, 8, 9].

- Processing nums[4] = 5, replace 8 in tails, updating it to [1, 4, 5, 9].
- Processing nums[5] = 6, update tails to [1, 4, 5, 6].
- Processing nums[6] = 7, update tails to [1, 4, 5, 6, 7].

Thus, the LIS length is 5.

#### **Implementation**

```cpp
int binarySearch(vector<int>& arr, int key) {
    int left = 0, right = arr.size()-1;
    while(left <= right) {
        int mid = left + (right - left)/2;
        if(key < arr[mid]) right = mid - 1;
        else if(key > arr[mid]) left = mid + 1;
        else return mid;
    }

    // returns the index where 'key' should be inserted to maintain sorted order
    return left; 
}

int lengthOfLIS(vector<int>& nums) {
    vector<int>tails;
    for(int i=0; i<nums.size(); i++){
        int index = binarySearch(tails, nums[i]);
        if(index == tails.size()) {
            // 'key' is greater than all elements in tails.
            tails.push_back(nums[i]); 
        }
        else tails[index] = nums[i];
    }
    return tails.size();
}
```

#### **Binary Search Explanation**

Why does Binary Search return left?

When the while(left <= right) loop exits:

- If key exists in arr, we return mid.
- If key does not exist in arr, left stops at the first index where the element is greater than or equal to key, which is exactly where key should be inserted.