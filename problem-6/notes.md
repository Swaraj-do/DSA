# Problem 6 — Palindrome Number

**Link:** https://leetcode.com/problems/palindrome-number/  
**Difficulty:** Easy  
**Platform:** LeetCode

---

## Approach

Reverse only the second half of the number and compare with first half.
No string conversion needed.

## Edge cases (handle first)

- x < 0 → always False (negative sign breaks palindrome)
- x % 10 == 0 and x != 0 → always False (ends in 0 but can't start with 0)

## Dry run — x=1221 (even length)

reversed_half=0,  x=1221 → take 1 → reversed_half=1,  x=122
reversed_half=1,  x=122  → take 2 → reversed_half=12, x=12
x == reversed_half → 12 == 12 → True

## Dry run — x=121 (odd length)

reversed_half=0,  x=121 → take 1 → reversed_half=1,  x=12
reversed_half=1,  x=12  → take 2 → reversed_half=12, x=1
x == reversed_half//10 → 1 == 1 → True

## Why stop at x > reversed_half?

When reversed_half catches up to x, we've processed exactly half the digits.

## Complexity

- Time: O(log n) — we process half the digits
- Space: O(1)