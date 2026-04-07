# Problem 9 — Reverse Integer

**Link:** https://leetcode.com/problems/reverse-integer/  
**Difficulty:** Medium  
**Platform:** LeetCode

---

## Approach

Pop last digit using x % 10, push onto rev using rev * 10 + digit.
Check for 32-bit overflow before every push.

## Key formula

pop:  digit = x % 10
      x = int(x / 10)

push: rev = rev * 10 + digit

## Overflow check

32-bit signed integer range: -2^31 to 2^31 - 1
= -2147483648 to 2147483647

Before pushing:
- if rev > 214748364 → overflow
- if rev == 214748364 and digit > 7 → overflow (INT_MAX ends in 7)
- if rev < -214748364 → overflow
- if rev == -214748364 and digit < -8 → overflow (INT_MIN ends in 8)

## Why int(x/10) instead of x//10?

Python // floors towards -infinity.
-123 // 10 = -13 (wrong)
int(-123 / 10) = -12 (correct)

## Dry run — x=123

digit=3, x=12, rev=3
digit=2, x=1,  rev=32
digit=1, x=0,  rev=321 ✓

## Complexity

- Time: O(log x) — number of digits in x
- Space: O(1)