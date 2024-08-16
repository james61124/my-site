---
title: "DP 系列 - The Rod Cutting Problem"
date: 2024-01-21
draft: false
author: "James"
tags:
  - Algorithm
  - Dynamic Programming
# image: /images/post.jpg
description: ""
toc: 
categories:
  - Algorithm
---

---------------------------------------------------------------------------------------------

如果賣出長度是 i 的 rod 可以得 p<sub>i</sub> 元，怎麼切一條長度是 n 的 rod 使總收入最大

---------------------------------------------------------------------------------------------

### **方法一、遞迴**
最直觀的方式就是用遞迴解，如下圖所示，r<sub>n</sub> 為切割長度 n 的 rod 可得的最大收入，假設 i 為最佳解中的第一段長度，<mark>r<sub>n</sub> = p<sub>i</sub> + r<sub>n-i</sub></mark>，因為 p<sub>i</sub> 是切割的最佳解中第一段的獲利，再加上剩餘部分最佳獲利就是我們要的答案。

i 怎麼求？利用迴圈讓 i 從 0 跑到 n-1，求出每一組 <mark>p<sub>i</sub> + r<sub>n-i</sub></mark>，找到最大的那組就是答案。

但這樣會遇到一個問題，每一次的 r<sub>n-i</sub> 都需要遞迴下去找到他的最佳解，這樣重複的 r 就會需要算很多次，以下圖為例，算 r<sub>4</sub> 的時候需要算 r<sub>3</sub>, r<sub>2</sub>, r<sub>1</sub>, r<sub>0</sub>，算 r<sub>3</sub> 又要再算一次 r<sub>2</sub>, r<sub>1</sub>, r<sub>0</sub>，因此我們需要利用 DP 來幫我們節省時間。

![Recursive](/images/posts/the-rod-cutting-problem/Recursive.jpg)


### **方法二、DP**

我們可以建表紀錄每一個 r<sub>i</sub> 的數值，這樣就不用每次遇到 i 都再算一次

已知 r<sub>0</sub>, r<sub>1</sub>，就可以利用 r<sub>0</sub>, r<sub>1</sub> 算 r<sub>2</sub>，<mark>r<sub>2</sub> = max( p<sub>1</sub>+r<sub>1</sub>, p<sub>2</sub>+r<sub>0</sub> )</mark>，再來利用 r<sub>1</sub>, r<sub>2</sub> 算 r<sub>3</sub>，最後就知道 r<sub>5</sub>，所以最重要的還是遞迴式 <mark>p<sub>i</sub> + r<sub>n-i</sub></mark>

![DP](/images/posts/the-rod-cutting-problem/DP.jpg)

### **小筆記**
建表紀錄遞迴中需要重複的部分，是 DP 裡很重要的工具！