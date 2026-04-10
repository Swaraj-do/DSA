# Problem 11 — Linear Search

**Link:** https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1  
**Difficulty:** Easy

---

## Approach

Loop from index 0 to n-1.
If element matches x, return that index.
If loop finishes without finding x, return -1.

## Dry run — arr=[1,2,3,4], x=3

i=0 → arr[0]=1 ≠ 3
i=1 → arr[1]=2 ≠ 3
i=2 → arr[2]=3 == 3 → return 2 ✓

## Complexity

- Time: O(n) — worst case check every element
- Space: O(1)