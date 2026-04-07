# LeetCode 268 - Missing Number
 
## Problem Summary
 
Given an array `nums` of `n` distinct numbers in the range `[0, n]`, find the one missing number.
 
---
 
## Approach: Gauss' Formula (Math)
 
### Core Idea
 
The sum of all integers from `0` to `n` is given by the formula:
 
```
expected_sum = n * (n + 1) / 2
```
 
If we subtract the actual sum of the array from this expected sum, the difference is the missing number.
 
```
missing = expected_sum - actual_sum
```
 
### Why This Works
 
Since all numbers in `[0, n]` are present except one, every number cancels out when subtracted — leaving only the missing one.
 
---
 
## Solution (Python)
 
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
```
 
---
 
## Walkthrough
 
**Example:** `nums = [3, 0, 1]`
 
- `n = 3`
- `expected = 3 * 4 / 2 = 6`
- `actual = 3 + 0 + 1 = 4`
- `missing = 6 - 4 = 2` ✅
 
---
 
## Complexity
 
| | Value |
|---|---|
| Time | O(n) — single pass to sum the array |
| Space | O(1) — no extra data structures used |
 
This satisfies the follow-up constraint for O(1) space and O(n) time.
 
---
 
## Alternative Approaches
 
### 1. XOR Trick
XOR every index and value together. Since `a ^ a = 0`, all paired values cancel, leaving the missing number.
 
```python
def missingNumber(self, nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```
 
- Time: O(n), Space: O(1)
- Clever but less readable than the math approach.
 
### 2. Sorting
Sort the array and check where `nums[i] != i`. Works but O(n log n) — not optimal.
 
### 3. Hash Set
Add all numbers to a set, then check which number from `0` to `n` is absent.
- Time: O(n), Space: O(n) — fails the O(1) space constraint.
 
---
 
## Key Takeaways
 
- **Gauss' formula** is the cleanest and most interview-friendly solution.
- Recognizing that a "missing element" problem maps to a sum difference is a useful pattern.
- XOR is a valid O(1) space alternative — good to know for bit manipulation questions.
- This pattern (expected vs actual) reappears in similar problems like **Find the Duplicate Number** and **Single Number**.
 
---
 
## Related Problems
 
| Problem | Connection |
|---|---|
| LeetCode 136 – Single Number | XOR trick |
| LeetCode 287 – Find the Duplicate Number | Sum / Floyd's cycle |
| LeetCode 41 – First Missing Positive | Missing number variant |