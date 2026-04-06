class Solution:
    def primeFac(self, n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
            i += 1  
        
        if n > 1:
            factors.append(n)
        
        return factors
        