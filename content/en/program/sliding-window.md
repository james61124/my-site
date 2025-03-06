---
title: "[ Algorithm ] Sliding Window | Core Concepts & Leetcode Problems Analysis"
date: 2025-03-05
draft: false
author: "James"
tags:
  - Sliding Window
  - Algorithms
  - Leetcode
image: /images/program/Algorithm.webp
description: ""
toc: 
categories:
  - Algorithm
---

The Sliding Window technique utilizes two pointers, left and right, to maintain a dynamic range (window). By shifting this window, we can reduce redundant computations, making it particularly useful for problems involving subarrays or substrings.

Sliding Window is categorized into two types:

1. Fixed-Size Sliding Window
2. Variable-Size Sliding Window

### **Fixed-Size Sliding Window**

- Used for problems that require subarrays or substrings of a fixed length.
- The window moves one step to the right at a time, removing the leftmost element and adding a new rightmost element.

#### **Example**

[[ Leetcode 1343 ] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-1343/)

#### **Template**

```cpp
int slidingWindow(vector<int>& arr, ...) {

    int left = 0;
    int right = 0;

    while( right < arr.size() ){
        
        // arr[right] push into the window

        if( right - left + 1 >= window_size ){

            // arr[left] pop out of the window

            left++;
        }
        right++;
    }
    return ...;
}
```

### **Variable-Size Sliding Window**

- Used for problems where we need to find the smallest or largest subarray/substring that satisfies a certain condition.
- Both left and right pointers adjust dynamically.

#### **Example**

[[ Leetcode 3 ] Longest Substring Without Repeating Characters | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-3/)

[[ Leetcode 209 ] Minimum Size Subarray Sum | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-209/)

[[ Leetcode 713 ] Subarray Product Less Than K | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-713/)

#### **Template**

```cpp
int slidingWindow(vector<int>& arr, ...) {

    int left = 0;
    int right = 0;

    while( right < arr.size() ){
        
        // arr[right] push into the window

        while( sliding window needs to shrink ){

            // arr[left] pop out of the window

            left++;
        }
        right++;
    }
    return ...;
}
```