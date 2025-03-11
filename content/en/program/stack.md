---
title: "[ Data Structure ] Stack & Monotone Stack | Core Concepts & Leetcode Problems Analysis"
date: 2025-03-07
draft: false
author: "James"
tags:
  - Stack
  - Monotone Stack
  - Data Structure
  - Leetcode
image: /images/program/Data-Structure.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

A Stack is a Last In, First Out (LIFO) data structure, similar to stacking blocks. The key characteristic is that you can only access the top element, and removal also happens only from the top. You cannot directly access elements below the top.

Common Stack Operations in C++ STL :

- **stack**<**int**>**st;** - Declare a stack
- **st.push(value);** - Insert an element at the top
- **st.pop();**	- Remove the top element (⚠️ Does not return the value)
- **st.top();**	- Return the top element (Does not remove it)
- **st.empty();** - Check if the stack is empty (returns true/false)
- **st.size();** - Get the number of elements in the stack

##### **Example**

[[ Leetcode 20 ] Valid Parentheses | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-20/)

[[ Leetcode 227 ] Basic Calculator II | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-227/)

### **Monotone Stack**

Next, let’s discuss a special type of stack—Monotone Stack. It is a concept rather than a built-in STL data structure. The key idea is to maintain a stack where elements are always in either increasing or decreasing order.

Imagine we want to maintain a decreasing stack.

```
stack = [8, 5, 3]
```

Push 6 into the Stack - Before pushing 6, we must pop 5 and 3 to maintain the decreasing order.

```
stack = [8]
```

Now, push 6 into the stack:

```
stack = [8, 6]
```

##### **Use Cases of Monotone Stack**

- Find the next greater/smaller element
- Find the previous greater/smaller element

##### **Example**

[[ Leetcode 496 ] Next Greater Element I | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-496/)

[[ Leetcode 739 ] Daily Temperatures | Solution Approach & Explanation](https://jamesblogger.com/program/leetcode-739/)