---
title: "[ Leetcode 496 ] Next Greater Element I | Solution Approach & Explanation"
date: 2025-03-06
draft: false
author: "James"
tags:
  - String
  - Stack
  - Math
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given two arrays nums1 and nums2, where nums1 is a subset of nums2, we need to find the next greater element for each number in nums1 within nums2.

Link🔗：[https://leetcode.com/problems/next-greater-element-i/](https://leetcode.com/problems/next-greater-element-i/)

### **Problem Analysis**

The key challenge is how to efficiently find the next greater element for each number in nums1 without iterating over nums2 repeatedly. A brute-force approach would be too slow, so we need an optimized method.

### **Solution - Monotone Stack**

The design of the Monotone Stack fits perfectly for this problem because we can ensure that the numbers in the stack are always in decreasing order. When iterating over the next number, if it's greater than the top of the stack, it means this is the next greater element for the stack's top. There are two problems to solve here:

##### **Building the Hash Map**

We cannot iterate over nums2 again for each number in nums1 to find the next greater element, so we must create a hash map to store the next greater element for each number in nums2—i.e., an unordered_map.

##### **Finding the Next Greater Element**

When iterating over the next number, if it's greater than the top of the stack, it means this is the next greater element for the stack's top. We then store this pair in the hash map and pop the top of the stack. We continue checking the stack until the current number is smaller than the top of the stack, and then push the current number into the stack.

##### **Final Cleanup**

At the end, all the elements left in the stack don't have a next greater element, so we fill them with -1 in the hash map, and then we can simply look up the values in the hash map.

**Time Complexity** - O( n )

**Space Complexity** - O( n )

##### **Implementation**
```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
    unordered_map<int, int>mp;
    stack<int>st;
    vector<int> ans;

    for( int num : nums2 ){
        while( !st.empty() && num > st.top() ) {
            mp[st.top()] = num;
            st.pop();
        }
        st.push(num);
    }

    while( !st.empty() ) {
        mp[st.top()] = -1;
        st.pop();
    }

    for( int num : nums1 ) {
        ans.push_back(mp[num]);
    }

    return ans;
}
```