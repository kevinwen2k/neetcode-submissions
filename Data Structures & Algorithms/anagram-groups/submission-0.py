class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}
        for s in strs:
            key = "".join(sorted(s))
            if output_dict.get(key) is None or len(output_dict.get(key)) == 0:
                output_dict[key] = []
            
            output_dict[key].append(s)

        return list(output_dict.values())


