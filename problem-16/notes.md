# Problem 16 — Second Largest

**Link:** https://www.geeksforgeeks.org/problems/second-largest3735/1  
**Difficulty:** Easy  
**Platform:** GeeksForGeeks

---

## Approach

Single pass with two variables: largest and second.
If x > largest → second = largest, largest = x
If x > second and x != largest → second = x
Return -1 if no second largest exists.

## Why x != largest?

To handle duplicates like [10, 10].
Second largest must be STRICTLY less than largest.

## Dry run — arr=[12, 35, 1, 10, 34, 1]

largest=-1, second=-1
x=12 → largest=12, second=-1
x=35 → second=12,  largest=35
x=1  → 1<35, 1>-1 and 1!=35 → second stays 12? 
       wait 1 < 12 so second stays 12
x=10 → 10<35, 10<12 → skip
x=34 → 34<35, 34>12 and 34!=35 → second=34
x=1  → skip
return 34 ✓

## Edge cases

- All same elements → return -1
- Only one element → return -1
- Two equal largest elements → return -1

## Complexity

- Time: O(n)
- Space: O(1)