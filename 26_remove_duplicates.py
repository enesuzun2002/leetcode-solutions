class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        left = 0
        for i in range(1, len(nums)):
            if nums[left] < nums[i]:
                nums[k] = nums[i]
                k += 1
                left = i
        return k
