---
title: "[ Leetcode 209 ] Minimum Size Subarray Sum | Solution Approach & Explanation"
date: 2025-01-29
draft: false
author: "James"
tags:
  - Sliding Window
  - Prefix Sum
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a positive integer array nums and a target value target, find the smallest contiguous subarray whose sum is greater than or equal to target. If no such subarray exists, return 0.

Link🔗：[https://leetcode.com/problems/minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/)

### **Method 1 - Sliding Window**

This problem can be solved using the Sliding Window technique. Since all numbers in the array are positive, we know that if a subarray sum reaches or exceeds target, adding more numbers will only make it longer but won't help find the shortest subarray. This means we can use a two-pointer approach to dynamically adjust the subarray range.

**Time Complexity** - O( n ), each element is processed at most twice—once when expanding right, and once when moving left.

**Space Complexity** - O( 1 ), Only a few integer variables are used for tracking indices and the sum.

##### **Step 1**

Use two pointers, left and right, to represent the current subarray:

- Expand right and add nums[right] to the sum until sum >= target.
- When sum >= target, attempt to minimize the subarray length by shrinking the left boundary.

##### **Step 2**

While sum >= target:

- Update minLength = min(minLength, right - left + 1).
- Move left to the right (left++) to check if we can find a smaller valid subarray.

##### **Step 3**

Repeat this process until right has scanned the entire array.

#### **Implementation**

```cpp
int minSubArrayLen(int target, vector<int>& nums) {
    int left = 0, sum = 0;

    // Initialize minLength with the maximum possible value
    int minLength = INT_MAX;

    for (int right = 0; right < nums.size(); right++) {
        sum += nums[right];
        
        while (sum >= target) {
            minLength = min(minLength, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }

    return (minLength == INT_MAX) ? 0 : minLength;
}
```

### **Method 2 - Binary Search + Prefix Sum**

This problem can also be solved using Prefix Sum + Binary Search. This method allows us to quickly calculate the sum of subarrays and efficiently find the shortest valid subarray using binary search.

**Time Complexity** - O( n log n )，We iterate through nums once (O(n)) and use binary search (O(log n)) for each index.

**Space Complexity** - O( n )，We need an additional prefix sum array.

##### **Step 1**

Construct a Prefix Sum array, where prefix[i] stores the sum of elements from nums[0] to nums[i-1]. This allows us to compute the sum of any subarray in constant time using prefix[j] - prefix[i].

##### **Step 2**

For each starting index i, use Binary Search to find the smallest index j such that:
- prefix[j] - prefix[i] + nums[i] >= target
- This ensures that the sum of the subarray nums[i] ~ nums[j] is at least target.

#### **Implementation**

```cpp
int binarySearch(vector<int>& arr, int target) {
    int left = 0, right = arr.size()-1;
    while(left <= right) {
        int mid = left + (right - left)/2;
        if( target < arr[mid] ) right = mid -1;
        else if( target > arr[mid] ) left = mid + 1;
        else return mid;
    }
    return left;
}

int minSubArrayLen(int target, vector<int>& nums) {
    int minLength = INT_MAX;
    vector<int>prefix(nums.size(), 0);
    prefix[0] = nums[0];
    for(int i=1; i<nums.size(); i++) {
        prefix[i] = prefix[i-1] + nums[i];
    }

    for(int i=0; i<nums.size(); i++){
        int index = binarySearch(prefix, target + prefix[i] - nums[i]);
        if(index != prefix.size()) minLength = min(index - i + 1, minLength);
    }
    return (minLength == INT_MAX) ? 0 : minLength;
}
```