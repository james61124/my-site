---
title: "[ Leetcode 219 ] Contains Duplicate II | Solution Approach & Explanation"
date: 2025-03-10
draft: false
author: "James"
tags:
  - Array
  - Hash Table
  - Sliding Window
  - Easy
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given an integer array **nums** and an integer **k**, determine whether there are two duplicate numbers whose indices have an absolute difference of at most **k**.

Link🔗：[https://leetcode.com/problems/contains-duplicate-ii/](https://leetcode.com/problems/contains-duplicate-ii/)

---

### **Solution - Hash Table**

The solution is intuitive: we store each number in a hash table and check if a duplicate exists since lookup in a hash table takes **O(1)** time on average. However, for this problem, we also need to track the index difference.

##### **Index Calculation**

Instead of only storing the numbers, we must also record their corresponding indices in the hash table. This allows us to calculate the difference between indices when we encounter duplicate numbers. We use `unordered_map` to store this mapping.

**Time Complexity** - O(n)

**Space Complexity** - O(n)

##### **Implementation**

```cpp
bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> umap;

    for (int i = 0; i < nums.size(); i++) {
        if (umap.find(nums[i]) != umap.end() && abs(umap[nums[i]] - i) <= k) return true;
        umap[nums[i]] = i;
    }

    return false;
}
```

### **Space Optimization - Unordered_set + Sliding Window**

While using unordered_map is straightforward, it requires storing both the key (number) and the value (index), which is not space-efficient. We can solve the problem without explicitly tracking indices.

##### **Optimized Approach**

We still insert numbers into an unordered_set. If the size of the set exceeds k, the earliest number becomes irrelevant because its index difference from the current index will be greater than k. We remove it from the set. This way, by maintaining a sliding window of size k, any duplicate found must satisfy the condition and we return true.

**Time Complexity** - O( n )

**Space Complexity** - O( n )

##### **Implementation**

```cpp
bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int>uset;

        for(int i=0; i<nums.size(); i++){
            if(uset.count(nums[i])) return true;
            else uset.insert(nums[i]);

            if(uset.size()>k) uset.erase(nums[i-k]);
        }

        return false;
    }
```