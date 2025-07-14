class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] != nums[i + 1]:
                c += 1
                if c == 3:
                    return nums[i]
        return nums[len(nums) - 1]
print("TEST 1: Expecting: 1, got: ", Solution().thirdMax([3,2,1]))
print("TEST 2: Expecting: 1, got: ", Solution().thirdMax([1,2]))
print("TEST 3: Expecting: 1, got: ", Solution().thirdMax([2,2,3,1]))