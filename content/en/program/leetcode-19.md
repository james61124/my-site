---
title: "[ Leetcode 19 ] Remove Nth Node From End of List | Solution Approach & Explanation"
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

Given a linked list, we need to delete the Nth node from the end and return the updated linked list.

Link🔗：[https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

### **Problem Analysis**

The key challenge is efficiently finding the Nth node from the end since searching in a linked list takes O(n) time.

### **Brute Force**

A straightforward approach would be to iterate through the list once while numbering each node. After determining the index of the node to delete, we would iterate again to locate and remove it. However, this approach is inefficient.

### **Solution - Fast and Slow Pointer**

We can use the **Fast and Slow Pointer** technique. If we set the initial distance between the fast and slow pointers to N, then when the fast pointer reaches the end of the list, the slow pointer will be positioned just before the node to be deleted.

Here are a few important considerations:

#### **Position of the Slow Pointer**

Since a linked list is singly linked, if the slow pointer points directly to the node that needs to be deleted, we won’t be able to remove it easily. Instead, we need the slow pointer to be positioned before the target node, so we can simply update **slow->next = slow->next->next** to remove the node.

#### **Initial Position of Pointers**

If the linked list contains only one node, and that node needs to be deleted, then the slow pointer must point to the node before the head. To achieve this, we create a **dummy** node pointing to the head, and both fast and slow pointers start from this **dummy** node.

#### **When Does the Fast Pointer Stop?**

The fast pointer stops when it reaches the last node (fast->next == nullptr). At this point, the slow pointer is correctly positioned just before the node to be deleted.

#### **Returning the Correct Pointer**

We should not return head directly because if the list contains only one node and it is deleted, the new list should be empty (nullptr). Instead, we return dummy->next.

**Time Complexity** - O( n ), since each element is traversed at most once by the fast pointer.

**Space Complexity** - O( 1 ), as we only use a dummy node.

#### **Implementation**

```cpp
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0);
    dummy.next = head;
    ListNode* fast = &dummy;
    ListNode* slow = &dummy;

    for(int i=0; i<n; i++){
        fast = fast->next;
    }

    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next;
    }

    slow->next = slow->next->next;
    return dummy.next;
}
```