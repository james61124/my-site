---
title: "[ Leetcode 11 ] Container With Most Water | 解題思路分享"
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

在一個 array 中，每個元素代表垂直線的高度，選擇兩條線，讓它們與 x 軸形成的容器能夠容納最多的水，並返回最大水量。

題目連結🔗：[https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

### **解題思路 - Opposite Direction Two Pointers**

這題的關鍵在於

```
容器的面積 = 短邊的高度 × 底邊的長度
```

我們希望找到兩條線，使這個面積最大。

#### **為什麼使用 Two Pointers？**

我們可以使用 Two Pointers，分別從數組的開頭 (left = 0) 和結尾 (right = arr.size()-1) 開始，逐步縮小範圍來尋找最大容積。

#### **如何選擇移動哪個指針？**

由於水的高度取決於較短的那一邊，我們計算當前區間的水量後，應該移動較矮的指針，因為移動較高的指針不會讓水位變高，但移動較矮的指針可能找到更高的線，進而增加水量。講具體一點，假設 left 比較低，這個時候如果拿 right 往內縮，如果下一個 height 比 left 高，計算 area 的時候還是會用 left*(變短的距離)，area 不會比較大，如果下一個 height 比 left 矮，那我們就是拿 (更小的 height)*(變短的距離)，area 也不會比較大，所以我們要移動較矮的 pointer。

**Time Complexity** - O( n )，每個元素最多被 right 或 left 掃過。

**Space Complexity** - O( 1 )，只使用了兩個指針

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