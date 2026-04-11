# Problem 17 — Best Time to Buy and Sell Stock

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
**Difficulty:** Easy  
**Platform:** LeetCode

---

## Approach

Single pass — track min price and max profit simultaneously.
For each price:
- if price < min_price → update min (better day to buy)
- else if price - min_price > max_profit → update profit

## Key insight

We don't need to try every pair (O(n²)).
The best profit on any day = today's price - lowest price before today.
Track the lowest price as we go → O(n).

## Why float('inf') for min_price?

So the first price always becomes the initial minimum.

## Dry run — prices=[7,1,5,3,6,4]

min=inf, profit=0
price=7 → min=7
price=1 → min=1
price=5 → profit=4
price=3 → 3-1=2 < 4 → skip
price=6 → profit=5
price=4 → 4-1=3 < 5 → skip
return 5 ✓

## Edge cases

- Prices only decrease → return 0 (no profit possible)
- Single price → return 0

## Complexity

- Time: O(n)
- Space: O(1)