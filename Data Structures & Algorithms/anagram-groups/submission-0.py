class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)
        for i, string in enumerate(strs):
            sorted_string = "".join(sorted(string))
            sorted_dict[sorted_string].append(i)

        final_list = []
        for string, indices in sorted_dict.items():
            same_words = []
            for index in indices:
                same_words.append(strs[index])
            final_list.append(same_words)
        return final_list
            