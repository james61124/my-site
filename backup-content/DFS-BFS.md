---
title: "[ Algorithm ] DFS & BFS | 核心概念與 Leetcode 題型解析"
date: 2025-03-08
draft: false
author: "James"
tags:
  - DFS
  - BFS
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

DFS 跟 BFS 都是要 iterate 一個 Graph 重要的技巧，這邊直接建立一個 Template 日後遇到就可以很快地 implement 出來。

### DFS ( Depth-First Search )

顧名思義深度優先，找到下一個 neighbor 不會剩下的 neighbor 看完，會先繼續往更深的 neighbor 走，才會再回來看完目前的 neighbor。

##### **Template**

```cpp
void DFS(vector<vector<int>>& arr, vector<bool>& visit, int v) {
    visit[v] = true;
    for( int neighbor : arr[v] ) {
        if(!visit[neighbor]) {
            DFS(arr, visit, neighbor);
        }
    }
}
```

### BFS ( Breadth-First Search )

廣度優先，所以會先看完所有的 neighbor，才會繼續往下看。

##### **Template**

```cpp
void BFS(vector<vector<int>>& arr, vector<bool>& visit, int start) {
    queue<int> q;
    visit[start] = true;
    q.push(start);

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int neighbor : arr[v]) {
            if (!visit[neighbor]) {
                visit[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}
```

### **範例**

