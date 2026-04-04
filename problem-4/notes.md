# Problem 4 — All Divisors of a Number

**Link:** https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1  
**Difficulty:** Easy

---

## Approach

Loop from 1 to sqrt(n) instead of 1 to n.
Divisors always come in pairs — if i divides n, then n/i also divides n.
Collect both at once, then sort and print.

## Why sqrt(n)?

If i * i <= n, then i and n/i are both divisors.
No need to go beyond sqrt(n) because the pairs cover the rest.

## Edge case

When i == n/i (perfect square like 36 → i=6), add only once to avoid duplicate.

## Complexity

- Time: O(sqrt(n))
- Space: O(1) — not counting the output list