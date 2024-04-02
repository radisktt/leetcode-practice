from typing import List

class Solution:
    @staticmethod
    def cnt(number: int) -> int:
        binary = bin(number)
        return binary.count('1')

    def custom_sort(self, index):
        return self.cnt(index), index

    def canSortArray(self, nums: List[int]) -> bool:
        arr1 = [self.cnt(num) for num in nums]
        stt = [i for i in range(1, len(nums)) if arr1[i] != arr1[i - 1]]

        # Sort the array using custom sorting based on stt array
        nums.sort(key=self.custom_sort)

        arr2 = [self.cnt(num) for num in nums]

        if arr1 != arr2:
            return False

        return True

