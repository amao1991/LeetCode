# Detect Capital

https://leetcode.com/problems/detect-capital/?tab=Description

## 題目

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".

2. All letters in this word are not capitals, like "leetcode".

3. Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

**Example 1:**

```
Input: "USA"
Output: True
```

**Example 2:**

```
Input: "FlaG"
Output: False
```

## 筆記

istitle(): title 就是只有字首大寫

islower(): 全小寫

isupper(): 全大寫

三個回傳的就已經是 True 或 False，用第二種方法直接 return 就好