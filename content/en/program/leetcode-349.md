---
title: "[ Leetcode 349 ] Intersection of Two Arrays | 解題思路分享"
date: 2025-02-23
draft: false
author: "James"
tags:
  - Array
  - Hash Table
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given two integer arrays nums1 and nums2, find their intersection, ensuring that each element appears only once in the result.

Link🔗：[https://leetcode.com/problems/intersection-of-two-arrays/](https://leetcode.com/problems/intersection-of-two-arrays/)

### **Solution - Hash Table**

The key idea here is simple: since we need to find the intersection, we need to check whether elements of one array exist in the other. To make this lookup operation O(1), we can first convert nums1 into an unordered_set, which acts as a hash table. This allows us to efficiently check whether elements of **nums2** exist in **nums1**.

If an element from **nums2** is found in the unordered_set, it is part of the intersection and should be added to the result vector. To avoid duplicates in the final result, we immediately erase the element from the unordered_set after finding it. Since erase() in an unordered_set is also O(1), the overall time complexity remains O(m + n).

**Time Complexity** - O( m + n ), since we iterate through both arrays once.

**Space Complexity** - O( m ), as we use an unordered_set and a vector for storing results.

### **Implementation**

```cpp
vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

    unordered_set<int> uset(nums1.begin(), nums1.end());
    vector<int> result;

    for( int num : nums2 ) {
        if(uset.count(num) > 0){
            result.push_back(num);
            uset.erase(num);
        }
    }

    return result;
}
```