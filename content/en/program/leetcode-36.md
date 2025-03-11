---
title: "[ Leetcode 36 ] Valid Sudoku | Solution Approach & Explanation"
date: 2025-03-10
draft: false
author: "James"
tags:
  - Array
  - Hash Table
  - Matrix
  - Medium
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a 9×9 Sudoku board, check whether the Sudoku configuration is valid. The conditions for validity are:

1. Each row must not contain duplicate numbers from 1 to 9.
2. Each column must not contain duplicate numbers from 1 to 9.
3. Each 3×3 sub-box must not contain duplicate numbers from 1 to 9.
4. The character '.' represents an empty cell and can be ignored.

Link🔗：[https://leetcode.com/problems/valid-sudoku/](https://leetcode.com/problems/valid-sudoku/)

### **Problem Analysis**

Essentially, we need to iterate through the entire board while minimizing the time spent checking for duplicate numbers. Using a Hash Table is an intuitive solution.

### **Solution - Hash Table**

Our goal is to efficiently track whether a given number has already appeared in a row, column, or box. While using three vector<unordered_set<int>> structures could work, it would consume more memory than necessary.
Since we only need to check if a number has appeared, a vector<vector<bool>> is more memory-efficient, where true indicates that a number has already been seen.

##### **Box Index Calculation**

Tracking duplicate numbers for rows and columns using a 2D vector is straightforward. If the number 5 appears at row i and column j, we simply mark row[i][5-1] and column[j][5-1] as true (subtracting 1 because indexes are 0-8, not 1-9).

However, the box index requires a little trick:

To represent each 3×3 sub-box with a unique index (0-8), we use:

```
(i/3)*3 + (j/3)
```

This transformation ensures each sub-box is assigned a unique index.

##### **Checking for Duplicates**

For a given number num at position (i, j), we check:

- row[i][num]
- column[j][num]
- box[boxIndex][num]

If any of these are already true, it means the Sudoku is invalid. Otherwise, we mark them as true to indicate the number has been seen.

**Time Complexity** - O( 27 ) = O( 1 )

**Space Complexity** - O( 27 ) = O( 1 )

##### **Implementation**

```cpp
bool isValidSudoku(vector<vector<char>>& board) {
    vector<vector<bool>>row(board.size(), vector<bool>(board[0].size(), false));
    vector<vector<bool>>col(board.size(), vector<bool>(board[0].size(), false));
    vector<vector<bool>>box(board.size(), vector<bool>(board[0].size(), false));

    for(int i=0; i<board.size(); i++){
        for(int j=0; j<board[0].size(); j++){
            if(board[i][j]=='.') continue;
            int num = board[i][j] - '1';
            int boxIndex = (i/3)*3 + (j/3);

            if(row[i][num]||col[j][num]||box[boxIndex][num]) return false;
            row[i][num] = true;
            col[j][num] = true;
            box[boxIndex][num] = true;
        }
    }

    return true;
}
```

### **Optimized Memory Usage  - Bitset**

While using vector<vector<bool>> is efficient, we can further optimize memory using bitset. Since we only store true/false values and the board size is fixed, bitset is a perfect fit.

##### **Implementation**

```cpp
bool isValidSudoku(vector<vector<char>>& board) {
    bitset<9>row[9];
    bitset<9>col[9];
    bitset<9>box[9];

    for(int i=0; i<board.size(); i++){
        for(int j=0; j<board[0].size(); j++){
            if(board[i][j]=='.') continue;
            int num = board[i][j] - '1';
            int boxIndex = (i/3)*3 + (j/3);

            if(row[i][num]||col[j][num]||box[boxIndex][num]) return false;
            row[i][num] = 1;
            col[j][num] = 1;
            box[boxIndex][num] = 1;
        }
    }

    return true;
}
```