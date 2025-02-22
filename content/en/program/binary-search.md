---
title: "Binary Search"
date: 2025-01-28
draft: false
author: "James"
tags:
  - Binary Search
  - Search Algorithms
  - Algorithms
image: /images/program/Algorithm.webp
description: ""
toc: 
categories:
  - Algorithm
---

Binary Search is a searching algorithm used to find the position of a key value in a sorted array. It works by repeatedly narrowing the search range in half, allowing it to quickly locate the target. As a result, the time complexity of Binary Search is O(logn).

### **Basic Steps**

1. Compare the target with the middle value. If they are equal, return the index.
2. If the target is less than the middle value, narrow the search range to the left half.
3. If the target is greater than the middle value, narrow the search range to the right half.
4. Repeat the steps above until the target is found or the search range is empty.

### **Calculating the Middle Index**

If you directly write <mark> int mid = (left + right) / 2 </mark>, the sum of left + right can overflow when both are large integers. So, it is safer to write <mark> int mid = left + (right - left) / 2 </mark>to avoid overflow.

### **Implementation**

{{< highlight cpp >}}
int binarySearch(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
{{< /highlight >}}

