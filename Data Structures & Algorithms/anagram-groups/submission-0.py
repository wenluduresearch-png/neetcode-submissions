class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_ls = dict()
        for s in strs:
            if ''.join(sorted(s)) in strs_ls:
                strs_ls[''.join(sorted(s))].append(s)
            else:
                strs_ls[''.join(sorted(s))] = [s]
        res = []
        for group in strs_ls.values():
            res.append(group)
        return res