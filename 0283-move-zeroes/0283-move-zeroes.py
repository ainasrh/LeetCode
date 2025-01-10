class Solution(object):
    def moveZeroes(self, nums):
      
        # Pointer to keep track of the position for non-zero elements
        non_zero_index = 0
        
        # Move all non-zero elements to the beginning of the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]  # Place the non-zero element at the correct index
                non_zero_index += 1  # Move the index forward for the next non-zero element

        # Fill the remaining elements with zero
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

    # No need to return anything, list is modified in place.

        