---
title: "[ Leetcode 167 ] Two Sum II - Input Array Is Sorted | Solution Approach & Explanation"
date: 2025-02-26
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

This problem is a variation of Two Sum. Given an array sorted in ascending order, the goal is to find two numbers whose sum equals the target value and return their 1-based indices.

Link🔗：[https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

### **Method - Opposite Direction Two Pointers**

This problem can be solved using opposite direction two-pointer technique, since this problem is about finding elements under certain constraints in a sorted array. Set left pointer at the first element and right pointer at the last element.

1. If the sum of the two numbers is greater than the target, move right
2. If the sum is smaller than the target, move left

**Time Complexity** - O( n ), Each element is at most traversed by either right or left.

**Space Complexity** - O( 1 ), Only two pointers are used.

#### **Implementation**

```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
    int left = 0;
    int right = numbers.size()-1;
    while(left <= right) {
        if(numbers[left] + numbers[right] < target) left++;
        else if(numbers[left] + numbers[right] > target) right--;
        else return {left+1, right+1};
    }
    return {};
}
```