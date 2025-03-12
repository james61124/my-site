---
title: "[ Leetcode 210 ] Course Schedule II | Solution Approach & Explanation"
date: 2025-03-10
draft: false
author: "James"
tags:
  - BFS
  - DFS
  - Graph
  - Topological Sort
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

You are required to complete **numCourses** courses, numbered from **0** to **numCourses - 1**. Some courses have prerequisites, represented by an array **prerequisites**, where **prerequisites[i] = [a, b]** means:

- To take course **a**, you must first complete course **b** (**b → a**).

The problem asks you to return a valid course order that allows you to complete all the courses. If it is **impossible** to finish all courses (i.e., if there is a **cycle** in the graph), return an **empty array []**.

Link🔗: [https://leetcode.com/problems/course-schedule-ii/](https://leetcode.com/problems/course-schedule-ii/)

---

### **Problem Analysis**

The task is to return a valid course order. If we represent the prerequisite relationships as a **Directed Graph**, the problem translates to **finding a topological order** of this graph, ensuring each course appears after its prerequisites.

### **Solution Approach - Topological Sort**

The key idea is to perform a **Topological Sort** on the directed graph. If you're familiar with Topological Sort, the implementation is straightforward. The only detail to pay attention to is:

#### **Use an Adjacency List for Better Implementation**

The input provides the **edges** of a directed graph. It's easier to work with if we first convert these edges into an **adjacency list**.

**Time Complexity** - O( V + E ), as we traverse the entire graph using **BFS**.

**Space Complexity** - O( V + E ), due to the construction of the **adjacency list**.

---

### **Implementation**

```cpp
vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses); // Adjacency list
    vector<int> in_degree(numCourses, 0); // Store in-degrees
    vector<int> order; // Store the result
    queue<int> q; // Queue for BFS

    // Build the graph and track in-degrees
    for (vector<int>& pre : prerequisites) {
        adj[pre[1]].push_back(pre[0]);
        in_degree[pre[0]]++;
    }

    // Add courses with 0 in-degree (no prerequisites) to the queue
    for (int i = 0; i < in_degree.size(); i++) {
        if (in_degree[i] == 0) {
            q.push(i);
        }
    }

    // Perform BFS
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        order.push_back(curr);

        for (int next : adj[curr]) {
            in_degree[next]--;
            if (in_degree[next] == 0) {
                q.push(next);
            }
        }
    }

    // If all courses are included in the order, return it; otherwise, return an empty array
    return (order.size() == numCourses) ? order : vector<int>();
}
