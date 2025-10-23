# LeetCode 49 - Group Anagrams
# Approach: Hashmap Counting
# Time Complexity: O(n^2 * k)
# Space Complexity: O(n * k)

class Solution(object):
    def groupAnagrams(self, words):
        Map = []

        for word in words:
            Hash = {}
            for letter in word:
                Hash[letter] = 1 + Hash.get(letter, 0)
            Map.append(Hash)
        # Calculate the number of letters in each word and store it in a dictionary,
        # then append it in a list called Map.

        Final = []
        Done = set()

        for i in range(len(Map)):
            anagram = []
            mots = ""
            for letter in Map[i]:  # Extract the letters from the dictionary and store them in a variable
                mots += letter
            if mots not in Done:  # Check if we already used this word
                anagram.append(mots)  # If it's not used, put it in the anagram list

            for j in range(i + 1, len(Map)):
                mots = ""
                for letter in Map[j]:
                    mots += letter  # Extract the letters from the dictionary and store them in a variable
                # If we didn’t already use it and the dictionaries are equal, append it to anagram
                if Map[i] == Map[j] and mots not in Done:
                    Done.add(mots)
                    anagram.append(mots)

            if len(anagram) > 0:  # If the anagram list is not empty, append it to the final list
                Final.append(anagram)

        return Final


# Example usage
solution = Solution()
Array = ["act", "pots", "tops", "cat", "stop", "hat"]
print(solution.groupAnagrams(Array))
