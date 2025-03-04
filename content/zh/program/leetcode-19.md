---
title: "[ Leetcode 19 ] Remove Nth Node From End of List | 解題思路分享"
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

給一個 linked list，要 delete 倒數第 n 個 node，並且 return 整個 linked list。

題目連結🔗：[https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

### **問題分析**

最重要的是要怎麼有效率的找到倒數第 n 個 node，因為 linked list 的 search 是 O(n)。

### **暴力解法 (Brute Force)**

如果先從頭 iterate 一次，還要編號，計算倒數第 n 個 index 是多少之後還要再 iterate 一次找到這個 node，太複雜了。

### **解題思路 - Fast and Slow Pointer**

我們可以直接使用 Fast and Slow Pointer，fast pointer 跟 slow pointer 的起始距離如果就是 n，那兩個 pointer 一起移動，fast 跑到底的時候 slow 就會剛好指在需要被 delete 的 node，這裡需要思考幾個問題:

#### **Slow Pointer 的位置**

Linked List 是單向的，如果 slow 指向需要被 detele 的 node，那我們沒有辦法 delete 這個 node，我們必須讓 slow->next 是我們要 delete 的 node，這樣 delete node 的時候才可以 slow->next = slow->next->next

#### **Pointers 起始位置**

如果整個 linked list 只有一個 node，而這個 node 必須被刪除，那 slow 就必須要指向 head 的前一個，所以 fast 跟 slow 的起始位置都不能是 head，而是要 create 一個 node **dummy** 來指向 head，然後從這裡開始。

#### **Fast 結束時機**

fast 的結束位置是在最後一個 node，也就是 fast->next 的時候，這樣 slow 才會剛好在需要被刪除的 node 的前一個。

#### **Return 的 Pointer**

返回的時候不能直接返回 head，因為如果整條 linked list 只有一個 node 而他也必須要刪除，那應該要返回 nullptr，所以直接返回 dummy->next 即可。

**Time Complexity** - O( n )，每個元素最多被 fast 掃過。

**Space Complexity** - O( 1 )，只使用了一個 dummy 的空間。

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