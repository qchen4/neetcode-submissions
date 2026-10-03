class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in wordMap:
                wordMap[key].append(word)
            else: 
                wordMap[key] = [word]
        return wordMap.values()