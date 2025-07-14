class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
      nums.sort()
      tof = False
      for i in range(len(nums) - 1):
          if nums[i] == nums[i + 1]:
              tof = True
              return True
      return False



