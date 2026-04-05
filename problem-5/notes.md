# Problem 5 — GCD of Two Numbers

**Link:** https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1  
**Difficulty:** Easy

---

## Approach

Euclidean algorithm — GCD(a, b) = GCD(b, a % b)
Keep replacing until b becomes 0, then a is the answer.

## Dry run — a=20, b=28

GCD(20, 28)
→ a=28, b=20%28=20  → wrong order so swap first
→ a=20, b=28%20=8
→ a=8,  b=20%8=4
→ a=4,  b=8%4=0
→ return 4 ✓

## Why it works

If d divides both a and b, it also divides a%b.
So GCD stays the same through every step.

## Complexity

- Time: O(log(min(a,b)))
- Space: O(1)