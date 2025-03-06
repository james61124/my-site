---
title: "[ Leetcode 21 ] Merge Two Sorted Lists | Solution Approach & Explanation"
date: 2025-03-05
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

Given a positive integer array nums and a positive integer k, find the number of subarrays whose product is less than k.

Link🔗：[https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)

### **Problem Analysis**

This problem is straightforward if you think from a two-pointer perspective. The key is to carefully determine which node points to which, and which pointer moves forward.

### **Solution - Two Pointers**

We need a pointer **cur** to track the last merged node. We compare the values of **list1** and **list2**, and link cur->next to the smaller one. There are a few important details to handle:

#### **Starting Node for cur**

Instead of writing an if-else statement to determine whether to start with list1 or list2, we can use a dummy node (ListNode dummy(0)).

- We initialize cur to point to this dummy node.
- Then, we simply compare the heads of list1 and list2 and proceed with merging.

#### **Handling the Remaining Nodes**

Once either list1 or list2 reaches nullptr, we can no longer compare values. However, the other list may still have remaining nodes.

- We simply attach cur->next to the remaining non-null list to ensure all nodes are included.

**Time Complexity** - O( n )

**Space Complexity** - O( 1 )

#### **Implementation**

```cpp
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode dummy(-1);
    ListNode* cur = &dummy;
    
    while(list1 && list2){
        if(list1->val <= list2->val){
            cur->next = list1; 
            list1 = list1->next;
        } else {
            cur->next = list2;
            list2 = list2->next;
        }
        cur = cur->next;
    }

    cur->next = list1 ? list1 : list2;
    return dummy.next;
}
```