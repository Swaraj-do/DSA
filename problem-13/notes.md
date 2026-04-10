# Problem 13 — Leaders in an Array

**Link:** https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1  
**Difficulty:** Easy

---

## Approach

Traverse from right to left, keep track of max seen so far.
If current element >= max_from_right, it's a leader.
Reverse result at end to restore left-to-right order.

## Why traverse from right?

A leader must be >= everything to its RIGHT.
Traversing right to left lets us track the running max
of everything we've already seen (which is to the right).

## Key insight

>= not just > because equal elements on right are allowed.

## Dry run — arr=[16, 17, 4, 3, 5, 2]

max=2,  add 2
i=4 → 5  >= 2  → add 5,  max=5
i=3 → 3  <  5  → skip
i=2 → 4  <  5  → skip
i=1 → 17 >= 5  → add 17, max=17
i=0 → 16 <  17 → skip
reverse → [17, 5, 2] ✓

## Edge cases

- Sorted increasing → only last element is leader
- Sorted decreasing → all elements are leaders

## Complexity

- Time: O(n)
- Space: O(1) — not counting output list