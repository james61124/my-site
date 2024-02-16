---
title: "Github 新手入門"
date: 2024-01-18
draft: false
author: "James"
tags:
  - Github
# image: /images/post.jpg
description: ""
toc: 
categories:
  - Github
---

# 什麼是 Github？
git 是版本控制的軟體，而 Github 是程式碼線上儲存平台，將專案存成一個個儲存庫 ( repository )，利用 git 來進行版本控制，也方便一個團隊來做協作

# 為什麼要使用 Github
> 一份專案我改 A，他改 B，我再改 C，非常容易打結
1. 可以存放大量自己的作品集
2. 可以輕鬆進行版本控制、分支何並追蹤能力
3. 免費且開源，可以參考並學習其他作者的開源碼

# 前置作業
1. 安裝 git

# 建立第一個 github repository
進入 github，點擊 your repository，點擊 new，填寫 Repository name，就可以 create 了
有兩個方式可以編輯剛剛建立的空的 repository：
1. 在 repository 建立檔案後 clone 到本地端
2. 直接將程式碼上傳至 repository


# clone 到本地端
repository 上隨便新增檔案，然後回來本地，開啟 terminal 輸入
```shell=1
git clone <repo-url>
```
再來就會看到本地端多了一個資料夾，然後修改過後就可以接著將修改的程式碼再上傳上來

# 將程式碼上傳至 repository
如果剛剛沒有 clone 空白的專案下來，可以先在電腦建立一個專案 ( 資料夾 )，或是你已經有一個你想要上傳的專案。terminal 進入這個資料夾後
```shell=1
git init
git remote add origin <repo-url>
git add .
git commit -m "your_commit"
git push origin master
```
簡單介紹一下各行意思
1. <mark>git init</mark> 就是建立一個 .git 的資料夾，任何版控的資訊都會透過他來儲存
2. <mark>git remote add origin</mark> github 那端的 repository 統稱叫做 remote 端，簡單來說就是讓本地資料夾跟 remote repository 連結，之後才可以 push 上去
3. <mark>git add .</mark> "." 是全部檔案的意思，意思就是將所有檔案狀態存到暫存器裡
4. <mark>git commit -m </mark> 要幫每一次提交的版本都下註解，your_commit 就是打上你自己的註解
5. <mark>git push origin master</mark> 就是將整個專案推到 repo，推到 master 這個預設的分支

# branch 介紹
首先我們先來了解甚麼是 branch，可以把 branch 想像成平行時空，他們可以互相獨立開發不影響彼此，那 branch 主要有三大功能：
1. 一個專案可能會經歷更新的過程，在更新的過程中想要定版備份舊功能又同時要開發新功能，就可以開新的 branch 實作，舊的 branch 擁有原本的功能，這樣就可以在不會影響到原本主功能的前提下實作新的功能
2. 多人開發時一人可以掌控一個 branch，各自開發完成 merge 起來即可，就不用同一份專案傳來傳去複製貼上程式碼
3. 在做學術研究時會碰到需要實驗不同的改動對於結果的影響，這時候就可以用 branch 來控制不同的功能，而不用把舊的功能 comment 掉才能跑新的功能

要先釐清一個概念，github 有分本地端跟遠端，本地做的任何改動在 push 上去之前都不會影響到遠端的變化，都只限在自己本地端，所以溝通時要很清楚我們在講的是 "本地" 端的 commit，"本地" 端的 branch，還是 "遠端" 的 commit，"遠端" 的 branch
再來介紹幾個常用的指令：
```shell=1
git branch
```
```git branch```可以知道現在有哪些 branch 以及現在在本地端的哪個 branch
```shell=1
git checkout [-b] <branch-name>
```
```git checkout```可以在本地端切換到另一個 branch，如果有加 -b 就是在本地端開啟一個新的 branch 並且切換過去
```shell=1
git push origin <branch-name>
```
最後就是把本地端 branch 資訊推到遠端