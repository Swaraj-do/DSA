# Problem 7 — Sum of All Divisors from 1 to N

**Link:** https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1  
**Difficulty:** Easy

---

## Naive approach (too slow)

For each i from 1 to n, find all divisors and sum them.
Time: O(n√n) — too slow for n=10^5

## Better approach — flip the question

Instead of: "what divisors does i have?"
Ask: "how many times does j appear as a divisor across all numbers 1 to n?"

Answer: j appears in j, 2j, 3j... → floor(n/j) times
So j contributes j * floor(n/j) to the total sum.

## Dry run — n=4

j=1 → 1 * (4//1) = 1 * 4 = 4
j=2 → 2 * (4//2) = 2 * 2 = 4
j=3 → 3 * (4//3) = 3 * 1 = 3
j=4 → 4 * (4//4) = 4 * 1 = 4
Total = 4+4+3+4 = 15 ✓

## Complexity

- Time: O(n)
- Space: O(1)