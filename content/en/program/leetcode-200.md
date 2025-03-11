---
title: "[ Leetcode 200 ] Number of Islands | Solution Approach & Explanation"
date: 2025-03-08
draft: false
author: "James"
tags:
  - DFS
  - BFS
  - Union Find
  - Disjoint Set
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a 2D array composed of '1' (land) and '0' (water), calculate the number of islands. An island is defined as a region of '1's (land) connected either horizontally or vertically, surrounded by '0's (water).

Link🔗：[https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

### **Solution - DFS**

This problem is straightforward. We iterate through the entire matrix and perform a DFS on each '1'. Since '0' does not need to be visited, if a node is visited during the same DFS, it means they belong to the same island. Therefore, the number of DFS calls we make will be equal to the number of islands.

##### **Will the time complexity be too high?**

In theory, we iterate once and perform DFS on each grid cell, so the time complexity would be O(n^2). However, since we mark the visited cells during DFS, which prevents revisiting them, each grid cell will only be visited once. Thus, the time complexity is actually O(n), where n is the number of grid cells.

##### **How to handle neighbors?**

Each grid can have at most four neighbors (up, down, left, right). We need to handle the boundary conditions to avoid segmentation faults.

```cpp
if( x > 0 && !visit[x-1][y] && grid[x-1][y] == '1' ) DFS(grid, visit, x-1, y); 
if( x < grid.size()-1 && !visit[x+1][y] && grid[x+1][y] == '1' ) DFS(grid, visit, x+1, y); 
if( y > 0 && !visit[x][y-1] && grid[x][y-1] == '1' ) DFS(grid, visit, x, y-1); 
if( y < grid[0].size()-1 && !visit[x][y+1] && grid[x][y+1] == '1' ) DFS(grid, visit, x, y+1); 
```

However, instead of writing four if statements, a more elegant solution is to store the four directions in an array and iterate through them. While this is slightly less efficient in terms of performance, it offers cleaner code. Below is an alternative implementation for reference.

```cpp
vector<vector<int>>direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
for(vector<int>& d : direction){
    if( x+d[0] >= 0 && x+d[0] < grid.size() && y+d[1] >= 0 && y+d[1] < grid[0].size() 
        && !visit[x+d[0]][y+d[1]] && grid[x+d[0]][y+d[1]] == '1' ) DFS(grid, visit, x+d[0], y+d[1]); 
}
```

**Time Complexity** - O( m x n ), where m and n are the dimensions of the grid, as we iterate through each cell exactly once.

**Space Complexity** - O( m x n ), due to the 2D array used to store the visited cells.

#### **Implementation**

```cpp
void DFS(vector<vector<char>>& grid, vector<vector<bool>>& visit, int x, int y){
    visit[x][y] = true;
    if( x > 0 && !visit[x-1][y] && grid[x-1][y] == '1' ) DFS(grid, visit, x-1, y); 
    if( x < grid.size()-1 && !visit[x+1][y] && grid[x+1][y] == '1' ) DFS(grid, visit, x+1, y); 
    if( y > 0 && !visit[x][y-1] && grid[x][y-1] == '1' ) DFS(grid, visit, x, y-1); 
    if( y < grid[0].size()-1 && !visit[x][y+1] && grid[x][y+1] == '1' ) DFS(grid, visit, x, y+1); 
}

int numIslands(vector<vector<char>>& grid) {
    vector<vector<bool>>visit(grid.size(), vector<bool>(grid[0].size(), false));
    int result = 0;

    for(int i=0; i<grid.size(); i++){
        for(int j=0; j<grid[0].size(); j++){
            if(!visit[i][j] && grid[i][j] == '1'){
                DFS(grid, visit, i, j);
                result++;
            }
        }
    }
    return result;
}
```

### **Alternative Solution - Union Find**

This problem can also be solved using the Union Find (Disjoint Set) data structure. Although it’s more complicated to implement, both methods have similar performance characteristics, so it’s a good learning exercise.

##### **Union Find**

Similar to DFS, we iterate through the 2D array. When encountering a '1', we perform a union operation. At the end, the number of disjoint sets will represent the number of islands.

##### **How to calculate the number of disjoint sets?**

The key is to track how many disjoint sets there are. We can maintain an integer **count**, which counts both the number of islands and water cells. Initially, count is set to the total number of grid cells, and each time a grid cell is united, we decrement count. We can also track the number of water cells as we iterate through the array. The final number of islands is count - numberOfWater.

##### **2D Array 在 Union Find 的 parent 中怎麼存放?**

vector<int>parent 存的是每一個對應的 grid 的 parent，問題是這個 vector 是 1D 的，我們的 grid 是 2D 的，因此可以利用 Linear Mapping 把 2D Array 轉成 1D 的 index。

```
index = i * n + j
```

**Time Complexity** - O( m × n × α(n) )，Unite 的操作是 α(n)，但是成長極為緩慢可以被忽略，基本上就是 O( m × n )

**Space Complexity** - O( m × n )，需要儲存 Union-Find 的 parent 和 rank array。

##### **Implementation**

```cpp
class UnionFind {
public:
    vector<int>parent;
    vector<int>rank;
    int count;

    UnionFind(int n){
        parent.resize(n);
        rank.resize(n, 0);
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
        count = n;
    }

    int find(int x){
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unite(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if( rootX != rootY ){
            if( rank[rootX] > rank[rootY] ){
                parent[rootY] = rootX;
            } else if( rank[rootY] > rank[rootX] ){
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            count--;
        }
    }
};

int numIslands(vector<vector<char>>& grid) {

    vector<vector<int>>direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int numberOfWater = 0;
    UnionFind uf(grid.size()*grid[0].size());

    for(int i=0; i<grid.size(); i++){
        for(int j=0; j<grid[0].size(); j++){
            if( grid[i][j] == '0' ) {
                numberOfWater++;
            } else {
                for(vector<int>& d : direction){
                    int neighbor_i = i + d[0];
                    int neighbor_j = j + d[1];
                    if( neighbor_i >= 0 && neighbor_i < grid.size() && neighbor_j >= 0 && neighbor_j < grid[0].size()
                        && grid[neighbor_i][neighbor_j] == '1' ) {
                        uf.unite( i*grid[0].size()+j, neighbor_i*grid[0].size()+neighbor_j ); 
                    }
                }
            }
        }
    }
    return uf.count - numberOfWater;
}
```