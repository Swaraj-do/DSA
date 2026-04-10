# Problem 12 — Largest Element in Array

**Link:** https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1  
**Difficulty:** Easy

---

## Approach

Start max_val as first element.
Loop from index 1, update max_val if current element is bigger.
Return max_val at end.

## Dry run — arr=[1, 8, 7, 56, 90]

max_val=1
i=1 → 8  > 1  → max_val=8
i=2 → 7  < 8  → skip
i=3 → 56 > 8  → max_val=56
i=4 → 90 > 56 → max_val=90
return 90 ✓

## Edge cases

- Single element → returns that element directly
- All same elements → returns that value

## Complexity

- Time: O(n)
- Space: O(1)