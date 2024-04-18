from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        # Add the first k elements to the min-heap
        for num in nums[:k]:
            heapq.heappush(min_heap, num)

        # Compare the rest of the elements in the list with min_heap
        # If the current element is greater than the smallest element in heap, then replace

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]


if __name__ == "__main__":
    nums_list_1 = [3, 2, 1, 5, 6, 4]
    fetch_position_1 = 2

    solution = Solution()

    result1 = solution.findKthLargest(nums=nums_list_1, k=fetch_position_1)
    print(f"{fetch_position_1}th largest element for {nums_list_1} is {result1}")

    nums_list_1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    fetch_position_1 = 4

    result2 = solution.findKthLargest(nums=nums_list_1, k=fetch_position_1)
    print(f"{fetch_position_1}th largest element for {nums_list_1} is {result2}")


