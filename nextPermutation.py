class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1) find pivot i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2) find j to swap with pivot
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3) swap
            nums[i], nums[j] = nums[j], nums[i]

        # 4) reverse suffix starting at i+1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
