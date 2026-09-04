class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for char in s:
            num_char = characters.get(char)
            if num_char is not None:
                characters[char] = num_char + 1
            else:
                characters[char] = 1
        for char in t:
            num_char = characters.get(char)
            if num_char is None:
                return False
            char_left = num_char - 1
            if char_left < 0:
                return False
            characters[char] = char_left
        for char, num in characters.items():
            if num is not 0:
                return False
        return True