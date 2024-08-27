---
title: "Insights from the 11th Meichu Hackathon"
date: 2024-02-17
draft: false
author: "James"
tags:
  - Hackathon
image: /images/MeiChuHackathon.jpg
permalink: "/life/11th-meichu-hackathon/"
description: ""
toc: 
categories:
  - Life
---

Due to my role as an organizer for the Meichu Hackathon over the past two years, it was only natural for me to return and participate again. Apart from gaining practical experience, I also wanted to see how the next generation of students prepared for the event.

## **Project Introduction**

### **Text Mode**

![image](/images/posts/11th-meichu-hackathon/text-mode-introduction.png)

This feature is designed for individuals with poor vision. Many elderly people often struggle to read small text, such as labels and instructions. To address this issue, we developed a text magnifier. Users can capture the text they need to read, and by using an image-to-text API, we can extract the text. We then use a large language model to reformat and present the information to the user. Additionally, users can ask questions about the text, such as: “What is the expiration date of this drink?” Our app, after processing the information, will provide the answer to help users retrieve the information they need.

### **Object Mode**

![image](/images/posts/11th-meichu-hackathon/object-mode-introduction.png)

This feature is aimed at enabling visually impaired individuals to live independently. The goal is to help users locate items through image recognition. Users specify what item they are looking for, and based on the image recognition results, the app provides directional cues, such as "turn left" or "turn right," to guide them to the item.

## **Technical Architecture**

![image](/images/posts/11th-meichu-hackathon/text-mode-technique.png)

For Text Mode, we use ML Kit to convert images to text and then employ a large language model with designed prompts to integrate the data and answer user queries.

![image](/images/posts/11th-meichu-hackathon/object-mode-technique.png)

For Object Mode, we use a lightweight Yolov5 model to determine object positions in images. This lightweight model runs directly on mobile devices, enabling offline processing and improved performance. We also use a customized dataset to fine-tune the model for more accurate object location detection.

## **Insights**

We were fortunate to be selected for the Google track, where the challenge was to design a user experience using the Android Accessibility API. This topic was particularly challenging for us, as there is limited scope for innovation in "accessibility apps." We considered many ideas, but struggled with two main issues: existing competition and the technical simplicity of our solutions, which didn’t favor the competition. The most challenging aspect of hackathons is not the implementation itself but coming up with a project that showcases both technical prowess and creativity while effectively addressing user pain points.

It took us a long time to decide on a project, and by the time we started working, we had only five days left. The most daunting part was that none of the five team members had experience with Android app development, which was a significant challenge. Despite learning a new skill, this hackathon truly felt like a hackathon—requiring us to complete a project in a very short timeframe, making trade-offs between quality and completeness. Our team put in our best effort to prepare for this competition, and it was a fantastic experience for me.

Having organized the event myself, I was very aware of all the details involved. Seeing the next generation of organizers under pressure was quite touching. Some participants may criticize the organizing team due to minor issues or lack of planning, but I believe constructive feedback is more valuable. The organizers work hard to make the event successful, and while there are always areas for improvement, harsh criticism is unnecessary. After a year of hard work, everyone deserves more understanding and helpful suggestions. This way, the event can continue to improve, and the world becomes a better place.



