class Solution:
    def groupAnagrams(self, strs: List[str]) ->     List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))   # e.g. "cat" -> "act"
            groups[key].append(word)

        return list(groups.values())