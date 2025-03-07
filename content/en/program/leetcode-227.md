---
title: "[ Leetcode 227 ] Basic Calculator II | Solution Approach & Explanation"
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

Given a string containing non-negative integers, +, -, *, /, and spaces, evaluate its value while following the standard order of operations (multiplication and division before addition and subtraction). The use of eval() is not allowed.

Link🔗：[https://leetcode.com/problems/basic-calculator-ii/](https://leetcode.com/problems/basic-calculator-ii/)

### **Problem Analysis**

Since multiplication and division must be processed before addition and subtraction, the problem requires handling Last In, First Out (LIFO) operations. This suggests that a stack would be an effective data structure to use.

### **Solution - Stack**

The intuitive approach is to use a stack, where we:

- Push numbers onto the stack when encountering + or -.
- Pop, compute, and push back when encountering * or /.

However, before implementing this, we need to handle some specific challenges:

#### **Extracting Multi-Digit Numbers**

Since numbers can have multiple digits, we need to accumulate digits into a single integer while iterating over the string.
This can be achieved using the following trick:

```cpp
for(char c : s){
    if( isdigit(c) ) {
        num = num * 10 + ( c - '0' );
    }
}
```

This ensures that num correctly stores the current complete integer before processing any operators.

#### **Handling Operators**

When we encounter an operator, we handle four cases:

1. If the previous operator was '+', push num onto the stack.
2. If the previous operator was '-', push -num onto the stack (so later summation is correct).
3. If the previous operator was '*', pop the top value from the stack, multiply it by num, and push it back.
4. If the previous operator was '/', pop the top value from the stack, divide it by num, and push it back.

Finally, we sum up all values in the stack to obtain the final result.

⚠️ Edge Case:
Since the last character in s is not an operator, the final number must be handled separately before exiting the loop.

**Time Complexity** - O( n ), since we iterate through the string once.

**Space Complexity** - O( n ), since we use a stack.

#### **Implementation**

```cpp
void updateParam( char& op, int& num, stack<int>& st) {
    switch( op ){
        case '+':
            st.push(num);
            break;
        case '-':
            st.push(-num);
            break;
        case '*':
            num *= st.top();
            st.pop();
            st.push(num);
            break;
        case '/':
            num = st.top() / num;
            st.pop();
            st.push(num);
            break;
    }
}

int calculate(string s) {
    int num = 0;
    char op = '+';
    int sum = 0;
    stack<int>st;

    for(char c : s){
        if( isdigit(c) ) {
            num = num * 10 + (c - '0');
        } else if( c != ' ' ) {
            updateParam(op, num, st);
            op = c;
            num = 0;
        } 
    }
    updateParam(op, num, st);

    while( !st.empty() ) {
        sum += st.top();
        st.pop();
    }

    return sum;
}
```

### **Optimized Solution - Space Reduction**

Observing the previous solution, we see that we only use the top of the stack at any given moment.
Instead of storing values in a stack, we can directly keep track of the current top number and accumulate previous sums.

This reduces space complexity to O(1) by introducing two new variables:

- **topNum** - stores the value that would be at the top of the stack.
- **result** - accumulates values that are already safe to sum.

**Time Complexity** - O( n ), since we still iterate through the string once.

**Space Complexity** - O( 1 ), as we eliminate the stack.

#### **Implementation**

```cpp
void updateParam( char& op, int& result, int& num, int& topNum ) {
    switch( op ){
        case '+':
            result += topNum;
            topNum = num;
            break;
        case '-':
            result += topNum;
            topNum = -num;
            break;
        case '*':
            topNum *= num;
            break;
        case '/':
            topNum /= num;
            break;
    }
}

int calculate(string s) {
    int result = 0;
    int num = 0;
    int topNum = 0;
    char op = '+';

    for(char c : s){
        if( isdigit(c) ) {
            num = num * 10 + (c - '0');
        } else if( c != ' ' ) {
            updateParam(op, result, num, topNum);
            op = c;
            num = 0;
        } 
    }

    updateParam(op, result, num, topNum);
    return result + topNum;
}
```