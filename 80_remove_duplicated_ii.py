# LeetCode - 80. Remove Duplicates from Sorted Array II
#
# Check if the list is empty and just return 0 to speed up the process
#
# Initialize k to 1. This will track the position to place the next valid element.
# Initialize m to 1. This will count occurrences of the current element.
#
# Loop through the list nums starting from the second element (index 1):
#     If the current element is the same as the previous element:
#         Increment the counter m.
#     Otherwise:
#         Reset m to 1 for the new element.
#     If m <= 2 (element appears at most twice):
#         Update nums[k] to the current element.
#         Increment k to move the position for the next valid element.
#
# Once the loop finishes, return k which represents the number of unique elements allowed.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # incase the list is empty
        if not nums:
            return 0

        # Initialize 'k' to track the count of unique elements
        k = 1

        # Initialize another counter that will keep track of same elements
        m = 1

        # Start looping through the list from the second element
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                m += 1
            else:
                m = 1  # Reset counter for a new element

            # Place the element if it is allowed (i.e., appears at most twice)
            if m <= 2:
                nums[k] = nums[i]
                k += 1
        # Return 'k' which is the count of unique elements
        return k
