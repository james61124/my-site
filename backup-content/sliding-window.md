---
title: "Sliding Window"
date: 2025-02-23
draft: false
author: "James"
tags:
  - Sliding Window
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Sliding Window 就是利用 left 和 right 兩個指標來維持一個動態區間 ( window )，透過移動這個 window 來減少重複運算，主要用在處理 subarray 或是 substring 之類的問題。

Sliding Window 分成兩種，Fixed-Size Sliding Window 跟 Variable-Size Sliding Window。

### Fixed-Size Sliding Window

- 適用於題目要求固定長度的 subarray 或是 substring
- 每次 window 向右滑動一格，去掉 left 舊 element，加入 right 的新 element

#### **Template**

- 適用於題目說滿足某條件的最小 / 最大 subarray 或是 substring
- left 跟 right 會動態調整

### 