---
title: "[ Leetcode 876 ] Middle of the Linked List | Solution Approach & Explanation"
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

Given a linked list, return the middle node.

Link🔗：[https://leetcode.com/problems/middle-of-the-linked-list/](https://leetcode.com/problems/middle-of-the-linked-list/)

### **Problem Analysis**

The goal is to find the middle node of the linked list.

### **Solution - Fast and Slow Pointer**

We use the Fast and Slow Pointer technique, where the fast pointer moves twice as fast as the slow pointer. When the fast pointer reaches the end, the slow pointer will be at the middle of the list.

#### **Starting Positions of the Two Pointers**

Both fast and slow pointers start at head.

- If the linked list has an even length, **fast->next == nullptr** when slow reaches the middle.
- If the linked list has an odd length, **fast == nullptr** when slow reaches the middle.

**Time Complexity** - O( n )，每個元素最多被 fast 掃過。

**Space Complexity** - O( 1 )

#### **Implementation**

```cpp
ListNode* middleNode(ListNode* head) {
    ListNode* fast = head;
    ListNode* slow = head;

    while(fast && fast->next){
        fast = fast->next->next;
        slow = slow->next;
    }
    return slow;
}
```