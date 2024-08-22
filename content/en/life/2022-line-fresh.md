---
title: "Insights from the 2022 LINE FRESH Competition"
date: 2024-02-20
draft: false
author: "James"
tags:
  - LINE FRESH
image: /images/LINE-FRESH.jpg
description: ""
toc: 
categories:
  - Life
---

## **Project Overview**

We designed a system called "Dida Dream - Timely Assistance System," aiming to achieve food redistribution by integrating a platform for near-expiry products with an online donation channel. Our main features include data collection of near-expiry products, customized notifications, donation plans, and a membership system.

### **Project Introduction**

#### **Data Collection of Near-Expiry Products**

![image](/images/posts/2022-line-fresh/data-collection-1.png)

![image](/images/posts/2022-line-fresh/data-collection-2.png)

We aimed to collaborate with chain and local businesses, integrating a backend database to collect all near-expiry product information. Chain stores served as the initial data source, with their APIs providing real-time updates on near-expiry products. For local shops, dedicated personnel handled data entry, and updates were made via our website.

#### **Customized Notifications**

![image](/images/posts/2022-line-fresh/customized-push-message-1.png)

![image](/images/posts/2022-line-fresh/customized-push-message-2.png)

![image](/images/posts/2022-line-fresh/customized-push-message-3.png)

We utilized LINE Bot to send regular notifications about discounts. These notifications were customized based on the data users provided during registration. Additionally, we introduced a psychological quiz called "You Are What You Eat" to personalize the style of the preview messages, enhancing user engagement.

#### **Donation Plan**

![image](/images/posts/2022-line-fresh/donate.png)

To achieve food redistribution, we used LINE Gift and instant coupons to connect Givers and Requesters, ensuring surplus food reaches those in need. Givers can send instant coupons through the system, which Requesters can redeem at specific stores after a real-time matching process. The Requester list is managed in collaboration with the government, using invitation codes to protect low-income individuals' privacy and to quickly promote our program. Givers are also incentivized with points through the Dida Collection loyalty card, encouraging more donations.

#### **Merchant Membership System**

Based on the amount of sponsorship, merchants receive badges like Bronze, Silver, and Gold, each offering different benefits such as search engine promotion and special projects.

### **Marketing Channels**

#### **Digital Media Promotion**

Both the Dida Collection loyalty card and the "You Are What You Eat" quiz feature one-click sharing options, increasing our exposure on social media. We also collaborated with NGOs and Key Opinion Leaders (KOLs) to broaden our reach.

#### **LINE Beacon**

We used LINE Beacon to push notifications from our official account, enabling users in areas near partner shops and chain stores to receive information about nearby near-expiry products.

### **Business Model**

Our main expenses include backend data maintenance and the cost of mass messaging via LINE Bot. On the revenue side, we generate income through merchant membership fees, large donation commissions, Beacon upgrade plans, government subsidies, and user contributions to create a sustainable financial model.

## **Technical Architecture**

![image](/images/posts/2022-line-fresh/techniques.jpg)

We built the official account using Django and integrated various LINE APIs. The LINE LIFF was connected to our official website, and the entire frontend and backend were deployed on a VPS using Apache Server. For initial data, we used the FamilyMart API to obtain current information.

## **Insights**

This was a long-term competition, taking about three months from initial concept to final project delivery. I believe LINE put a lot of effort into preparing for this campus competition, holding numerous workshops that taught us about business models and project ideation. They also provided mentors to discuss the feasibility and completeness of our projects, helping us understand which aspects LINE prioritizes in this competition.

LINE's main goal in organizing this competition was likely to encourage cross-disciplinary collaboration, combining technical and business talents to spark new ideas. I was fortunate that my team members each had their strengths and were well-suited for their roles. Since we were all from the Computer Science department, we were familiar with time management and collaboration methods.

This competition was my first experience working on a large-scale project. Previously, I had only completed classroom assignments, so I was delighted that everyone took the time to seriously prepare for this competition. Winning a prize became secondary to me; what mattered most was the significant technical progress we made and how this experience made me less intimidated by large projects. Although the technologies we used seem simple in hindsight, they were essential steps in our growth, adding another branch to our skill tree.