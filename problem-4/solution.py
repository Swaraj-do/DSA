#User function Template for python3
import math

class Solution:
    def print_divisors(self, N):
         divisors=[]
         
         for i in range(1,int(math.sqrt(N))+1):
             if N % i==0:
                 divisors.append(i)
                 if i != N//i:
                     divisors.append(N//i)
            
         divisors.sort()
         
         for d in divisors:
             print(d, end=" ")
                 