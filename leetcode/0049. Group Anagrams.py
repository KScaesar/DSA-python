from typing import List


class Solution:
    # https://leetcode.com/problems/group-anagrams/

    # 沒難度 複習可跳過
    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            # group = tuple(sorted([c for c in word]))
            group = tuple(sorted(word))
            if group in groups:
                groups[group].append(word)
            else:
                groups[group] = [word]

        return list(groups.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams_v1(["eat", "tea", "tan", "ate", "nat", "bat"]))
