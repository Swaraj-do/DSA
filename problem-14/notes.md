# Problem 14 — Rotate Array by One

**Link:** https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1  
**Difficulty:** Easy

---

## Approach

Save last element.
Shift all elements one step to the right (from right to left).
Place saved element at index 0.

## Why loop right to left?

If we loop left to right, arr[i-1] would already be
overwritten before we copy it. Right to left is safe.

## Dry run — arr=[1,2,3,4,5]

last=5
i=4 → arr[4]=arr[3] → [1,2,3,4,4]
i=3 → arr[3]=arr[2] → [1,2,3,3,4]
i=2 → arr[2]=arr[1] → [1,2,2,3,4]
i=1 → arr[1]=arr[0] → [1,1,2,3,4]
arr[0]=5 → [5,1,2,3,4] ✓

## Edge cases

- Single element → stays the same
- All same elements → stays the same

## Complexity

- Time: O(n)
- Space: O(1)