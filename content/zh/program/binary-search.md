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

Binary Search 就是一種 searching algorithm，用來在一個 sorted array 中尋找 key value 的位置，主要是透過每次將搜尋範圍縮小一半來快速定位目標，所以 Binary Search 的 Time Complexity 為 O(log n)。

### **基本步驟**

1. 比較 target 與 middle 的值，如果相等則 return index。
2. 如果 target 小於 middle 的值，縮小搜尋範圍至左半部分。
3. 如果 target 大於 middle 的值，縮小搜尋範圍至右半部分。
4. 重複以上步驟，直到找到 target 或搜尋範圍為空。

### **middle 的計算**

如果直接寫 <mark> int mid = (left + right) / 2 </mark>，left + right 在 int 太大的時候就會 overflow，所以應該要寫成 <mark> int mid = left + (right - left) / 2 </mark>

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

