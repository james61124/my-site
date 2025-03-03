---
title: "[ Leetcode 26 ] Remove Duplicates from Sorted Array | Solution Approach & Explanation"
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

Given an ascending sorted array - nums, the task is to remove duplicate elements in place so that each element appears only once and return the new length of the array.

⚠ Requirements：
1. Extra array space cannot be used; modifications must be done in place.
2. If the returned array length is k, it means the first k elements of nums contain the result after removing duplicates, while the remaining elements can be arbitrary and do not need to be considered.

Link🔗：[https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

### **Solution - Fast and Slow Pointers**

#### **Why Use Two Pointers?**

We can use the Two Pointers technique where:
- The **Fast Pointer** traverses the entire array.
- The **Slow Pointer** marks the position of the last unique element found after removing duplicates.

👉 Fast pointer keep moving forward. When nums[fast] != nums[slow], it means a new unique element is found, so it should be stored at the position of slow, and slow moves forward.

**Time Complexity** - O( n ), as each element is checked at most once by fast.

**Space Complexity** - O( 1 ), since only two pointers are used.

#### **Implementation**

```cpp
int removeDuplicates(vector<int>& nums) {
    int slow = 0;
    int fast = 1;
    while(fast < nums.size()){
        if(nums[slow]!=nums[fast]){
            slow++;
            nums[slow]=nums[fast];
        }
        fast++;
    }
    return slow+1;
}
```