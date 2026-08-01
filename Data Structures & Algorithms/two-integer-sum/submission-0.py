class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        new_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in new_map:
                return [new_map[complement], i]
            new_map[nums[i]] = i