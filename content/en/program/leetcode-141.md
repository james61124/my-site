---
title: "[ Leetcode 141 ] Linked List Cycle | Solution Approach & Explanation"
date: 2025-03-03
draft: false
author: "James"
tags:
  - Linked List
  - Two Pointers
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given a linked list, determine whether it contains a cycle.

Link🔗：[https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)

### **Solution - Fast and Slow Pointers ( Floyd's Cycle Detection Algorithm )**

This is one of the classic problems for detecting a cycle in a linked list. The idea is to use two pointers, where the fast pointer moves twice as fast as the slow pointer. If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

**Time Complexity** - O( n ), since each node is visited at most once.

**Space Complexity** - O( 1 )

#### **Implementation**

```cpp
bool hasCycle(ListNode *head) {
    ListNode* fast = head;
    ListNode* slow = head;

    while(fast && fast->next){
        fast = fast->next->next;
        slow = slow->next;
        if(slow == fast) return true;
    }
    return false;
}
```