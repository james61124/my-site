---
title: "[ Leetcode 841 ] Keys and Rooms | Solution Approach & Explanation"
date: 2025-01-29
draft: false
author: "James"
tags:
  - DFS
  - Algorithms
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

There are n rooms labeled from 0 to n-1. Each rooms[i] contains a list of keys that can be used to unlock other rooms. Initially, you start in room 0, which is already unlocked. The goal is to determine whether you can visit all rooms.

Link🔗：[https://leetcode.com/problems/keys-and-rooms/](https://leetcode.com/problems/keys-and-rooms/)

### **Solution - DFS**

This problem can be solved using Depth-First Search (DFS), as it is essentially a graph traversal problem. The rooms and their keys form a directed graph, where a key in rooms[i] represents an edge from room i to another room.

### **Implementation**

```cpp

void DFS(vector<vector<int>>& arr, vector<bool>& visit, int v) {
    visit[v] = true;
    for( int neighbor : arr[v] ) {
        if(!visit[neighbor]) {
            DFS(arr, visit, neighbor);
        }
    }
}

bool canVisitAllRooms(vector<vector<int>>& rooms) {
    vector<bool>visit(rooms.size(), false);
    DFS(rooms, visit, 0);
    for( bool element: visit ) {
        if( !element ) return false;
    }
    return true;
}

```