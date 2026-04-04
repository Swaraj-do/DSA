class Solution:
    def armstrongNumber(self, n):
        digits = [int(d) for d in str(n)]
        return sum(d**3 for d in digits) == n