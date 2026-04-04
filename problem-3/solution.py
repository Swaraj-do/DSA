class Solution:
    def evenlyDivides(self, n):
        return sum(1 for d in str(n) if int(d) != 0 and n % int(d) == 0)