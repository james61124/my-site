---
title: "[ Leetcode 739 ] Daily Temperatures | Solution Approach & Explanation"
date: 2025-03-06
draft: false
author: "James"
tags:
  - String
  - Stack
  - Math
  - Leetcode
image: /images/program/Leetcode.jpeg
description: ""
toc: 
categories:
  - Algorithm
---

Given an integer array **temperatures**, representing the temperature on each day, for each day, we need to find the nearest future day with a higher temperature and return the number of days between the current day and that day. If there is no higher temperature in the future, return 0.

Link🔗：[https://leetcode.com/problems/daily-temperatures/](https://leetcode.com/problems/daily-temperatures/)

### **Problem Analysis**

The key to this problem is finding the next number greater than the current one, so we can directly think of using a Monotone Stack.

### **Solution - Monotone Stack**

The design of a Monotone Stack fits this problem perfectly, because we can design the stack to maintain a decreasing order. Thus, when we encounter a number that is greater than the stack's top element, it indicates that this is the next greater element for the stack's top element. Building on this idea, we can proceed further:

##### **Choice of Storing Numbers in the Stack**

We will use a Monotone Stack to store the temperatures and iterate through the temperatures to find the next greater element. The issue is that the problem asks us to store the difference in indices between the current day and the next greater day. So, instead of just storing the next greater element in the hash map, which wouldn't give us the index difference, we can think differently: we can directly store the index in the stack.

When we need to push an element into the stack, we push its index. Then, when comparing the current element with temperatures[st.top()], we can easily find the index difference.

##### **Displaying the Result**

Finally, we need to store the index difference between the current day and the next greater element in a vector. We can initialize a vector with 0s and update it with the index difference when we find the next greater element. If an element isn't updated, it means it doesn't have a next greater element, so it remains 0.

**Time Complexity** - O( n ), since we only iterate over the **temperatures** array once.

**Space Complexity** - O( n ), as we only need a stack and a 1D vector.

#### **Implementation**
```cpp
vector<int> dailyTemperatures(vector<int>& temperatures) {
    stack<int>index;
    vector<int>result(temperatures.size(), 0);

    for(int i=0; i<temperatures.size(); i++){
        while( !index.empty() && temperatures[i] > temperatures[index.top()]) {
            result[index.top()] = i - index.top();
            index.pop();
        }
        index.push(i);
    }

    return result;
}
```


