# LeetCode - 26. Remove Duplicates from Sorted Array
#
# Initialize k to 1. This will track the count of unique elements.
#
# Set left to 0. This will track the index of the last unique element found.
#
# Loop through the list nums starting from the second element (index 1):
#     If the current element is greater than the last unique element (located at nums[left]):
#         Update nums[k] to the current element, as this is a unique element.
#         Increment k by 1, to move the position for the next unique element.
#         Set left to the current index i, since this is now the last unique element.
#
# Once the loop finishes, return k which represents the number of unique elements found.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize 'k' to track the count of unique elements
        k = 1

        # 'left' points to the index of the last unique element found
        left = 0

        # Start looping through the list from the second element
        for i in range(1, len(nums)):
            # Check if the current element is greater than the last unique element
            if nums[left] < nums[i]:
                # Place the current element at index 'k' as it's unique
                nums[k] = nums[i]

                # Increment 'k' to point to the next position for unique elements
                k += 1

                # Update 'left' to point to the current index as it's the last unique element
                left = i

        # Return 'k' which is the count of unique elements
        return k
