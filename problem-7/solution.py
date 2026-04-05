class Solution:
    def sumOfDivisors(self, n):
        total = 0
        
        for j in range(1, n + 1):
            total += j * (n // j)  
        
        return total