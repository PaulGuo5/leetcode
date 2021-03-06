class Solution:
    def findMin1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[mid]
    
    def findMin(self, nums: List[int]) -> int:   
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]
