class Solution:
    def leaders(self, arr):
        result = []
        max_from_right = arr[-1]
        result.append(arr[-1])
        
        for i in range(len(arr) - 2, -1 , -1 ):
            if arr[i]>= max_from_right:
                result.append(arr[i])
                max_from_right = arr[i]
                
        result.reverse()
        return result