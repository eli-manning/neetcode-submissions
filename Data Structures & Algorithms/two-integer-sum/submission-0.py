class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if nums_seen.get(complement) is not None:
                return [nums_seen[complement], i]
            nums_seen[nums[i]] = i
