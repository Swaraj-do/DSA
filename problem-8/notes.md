# Problem 8 — Unique Prime Factors

**Link:** https://www.geeksforgeeks.org/problems/prime-factors5052/1  
**Difficulty:** Easy

---

## Approach

Trial division up to sqrt(n).
For each i starting from 2:
- if i divides n → i is a prime factor, add it once
- strip all copies of i from n
- move to next i
If n > 1 after loop → n itself is prime, add it

## Why only up to sqrt(n)?

Every composite number has at least one factor ≤ sqrt(n).
So if nothing divides n up to sqrt(n), n must be prime.

## Why no need to check if i is prime?

By the time we reach i, all smaller factors are already
divided out. So if i still divides n, it has to be prime.

## Dry run — n=60

i=2 → add 2 → 60→30→15
i=3 → add 3 → 15→5
i=4 → skip
loop ends (i*i > 5), n=5 > 1 → add 5
Output: [2, 3, 5] ✓

## Complexity

- Time: O(sqrt(n))
- Space: O(1) — not counting output list