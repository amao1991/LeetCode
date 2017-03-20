# Hamming Distance

https://leetcode.com/problems/hamming-distance/#/description

## 題目

The [Hamming distance](https://www.wikiwand.com/en/Hamming_distance) between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, calculate the Hamming distance.

**Example**

```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

## Hamming Distance

[中文版XD](https://www.wikiwand.com/zh-tw/%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB)

直接上範例

* 1011101與1001001之間的漢明距離是2。
* 2143896與2233796之間的漢明距離是3。
* "toned"與"roses"之間的漢明距離是3。

## Note

**count()**

```
str.count('sub')
```

計算字串 str 中，sub 出現的次數