class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        reverse_sorted_dict = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        k_elements = []
        for key, value in reverse_sorted_dict.items():
            if k <= 0:
                return k_elements
            k_elements.append(key)
            k -= 1

        return k_elements
            