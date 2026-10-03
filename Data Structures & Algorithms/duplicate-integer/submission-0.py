class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        old = []
        for num in nums:
            for old_num in old:
                if num == old_num:
                    return True
            old.append(num)
        return False
         