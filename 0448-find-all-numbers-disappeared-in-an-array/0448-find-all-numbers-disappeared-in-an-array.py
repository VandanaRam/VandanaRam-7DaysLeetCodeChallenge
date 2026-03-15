class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    # Mark presence by negating values at specific indices
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] *= -1
            
    # Collect indices that remained positive
        return [i + 1 for i, num in enumerate(nums) if num > 0]

        
        