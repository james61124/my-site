---
title: "[ Leetcode 11 ] Container With Most Water | Solution Approach & Explanation"
date: 2025-02-27
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

In a given array, each element represents the height of a vertical line. The task is to choose two lines such that the container formed with the x-axis can hold the maximum amount of water and return that maximum volume.

Link🔗：[https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

### **Solution - Opposite Direction Two Pointers**

The key idea is that the area of the container is determined by: 

```
Area = min(Height of left, Height of right) × Distance between them
```

We aim to find two lines that maximize this area.

#### **Why Use Two Pointers?**

We can use the **Two Pointers** approach, starting with one pointer at the beginning (left = 0) and another at the end (right = arr.size() - 1). By gradually narrowing the range, we can efficiently find the maximum container volume.

#### **How to Decide Which Pointer to Move?**

Since the height of the container is determined by the shorter side, after computing the current area, we should move the pointer pointing to the shorter height. Moving the taller pointer won't increase the water level, but moving the shorter pointer might find a taller line, potentially increasing the area.

To be specific, if left is shorter than right, then shrinking right inward won't improve the area. If the new height[right] is taller than left, the calculated area will still be limited by left. If the new height[right] is shorter, then the area will be even smaller. Hence, we always move the pointer pointing to the shorter height.

**Time Complexity** - O( n ), as each element is checked at most once by either right or left.

**Space Complexity** - O( 1 ), since only two pointers are used.

#### **Implementation**

```cpp
int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size()-1;
    int maxArea = 0;

    while(left < right){
        int smallerHeight = min(height[left], height[right]);
        maxArea = max(maxArea, smallerHeight*(right-left));
        if(height[left]<height[right]) left++;
        else right--;
    }
    return maxArea;
}
```