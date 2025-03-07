---
title: "[ Leetcode 713 ] Subarray Product Less Than K | Solution Approach & Explanation"
date: 2025-03-05
draft: false
author: "James"
tags:
  - Array
  - Sliding Window
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a positive integer array **nums** and a positive integer **k**, find the number of subarrays whose product is less than **k**.

Link🔗：[https://leetcode.com/problems/subarray-product-less-than-k/](https://leetcode.com/problems/subarray-product-less-than-k/)

### **Problem Analysis**

When I see a problem involving a constraint on the subarray's size but with a flexible range, I immediately consider using a variable-size sliding window approach. The key question here is: how should we move the left and right pointers to ensure we capture all valid subarrays without missing any?

### **Solution - Variable-Size Sliding Window**

Using the sliding window technique, we need to determine when to move the left pointer while iterating with right. The approach involves:

1. Using **left** and **right** pointers to define the sliding window boundaries.
2. Maintaining a variable **currentProduct** to store the product of elements within the window.
3. Storing the count of valid subarrays in **result**.

#### **When to Move the Left Pointer?**

Each time we extend the window by moving **right**, we multiply nums[right] into **currentProduct**. However, if **currentProduct** becomes ≥ k, we need to shrink the window from the **left** by continuously dividing nums[left] out of currentProduct until it becomes < k again.

#### **Preventing Left from Exceeding Right**

If the sliding window contains only one element (i.e., left == right), and currentProduct is still ≥ k, we must handle this case carefully. Otherwise, left might keep moving right indefinitely, surpassing right.

Thus, we need to add a condition in the while loop to ensure that left does not surpass right (left < right).

#### **How to Count the Number of Valid Subarrays?**

The key observation is that whenever we find a valid sliding window [left, right], all subarrays ending at right within this window are also valid.

For example, if the sliding window is [4, 5, 8] and k = 200, then all subarrays ending at right are valid:

- [8]
- [5, 8]
- [4, 5, 8]

Thus, we should add the size of the sliding window (right - left + 1) to result, since some of these subarrays will no longer be visible as right moves forward.

If the window contains only one element and currentProduct is still ≥ k, we don't increment result and simply continue iterating.

**Time Complexity** - O( n )

**Space Complexity** - O( 1 )

#### **Implementation**

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
    int left = 0;
    int right = 0;
    int currentProduct = 1;
    int res = 0;

    while(right < nums.size()){
        currentProduct *= nums[right];
        while(currentProduct >= k && left<right){
            currentProduct /= nums[left];
            left++;
        }
        if(currentProduct < k) res += (right-left+1);
        right++;
    }
    return res;
}
```