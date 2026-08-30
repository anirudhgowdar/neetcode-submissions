class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexMap:
                return sorted([i, indexMap[diff]])
            else:
                indexMap[nums[i]] = i