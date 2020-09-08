class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j = n-1
        while j-1 >= 0 and arr[j-1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        
        res = j
        for i in range(n):
            if i-1 >= 0 and arr[i-1] > arr[i]:
                break
            while j < n and arr[j] < arr[i]:
                j += 1
            res = min(res, j-i-1)
        return res
