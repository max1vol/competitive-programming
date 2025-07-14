class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        c = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                if c >= 2 / len(nums):
                    return nums[i]
                else:
                    c = 0
        else:
            c += 1

