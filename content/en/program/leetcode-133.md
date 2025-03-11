---
title: "[ Leetcode 133 ] Clone Graph | Solution Approach & Explanation"
date: 2025-03-08
draft: false
author: "James"
tags:
  - DFS
  - BFS
  - Graph
  - Hash Table
  - Medium
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

The task is to clone a graph, but we cannot directly return the pointer to the original graph.

Link🔗：[https://leetcode.com/problems/clone-graph/](https://leetcode.com/problems/clone-graph/)

### **Solution - DFS**

This problem is essentially about using DFS to traverse the entire graph and clone all the nodes. The main challenge is where to store the cloned nodes during the DFS traversal.

##### **Design of the visit map**

If we use the usual vector<bool> to track visited nodes, we will only know if a node has been visited but not where the cloned node is. Therefore, we should use an unordered_map to store the mapping between the original node and the cloned node. This way, if a Node* is found in the unordered_map, it means the node has been visited, and we can directly find the corresponding cloned node.

**Time Complexity** - O( V + E ), where V is the number of nodes and E is the number of edges.

**Space Complexity** - O( V ), as we create an unordered_map to store the node mapping.

#### **Implementation**

```cpp
Node* DFS(Node* node, unordered_map<Node*, Node*>&visit){
    if(!node) return nullptr;
    if(visit[node]) return visit[node];

    vector<Node*>cloneNeighbors;
    Node* cloneNode = new Node(node->val, cloneNeighbors);
    visit[node] = cloneNode;

    for(Node* next : node->neighbors) {
        cloneNode->neighbors.push_back(DFS(next, visit));
    }

    return cloneNode;
}

Node* cloneGraph(Node* node) {
    unordered_map<Node*, Node*>visit;
    return DFS(node, visit);
}
```

