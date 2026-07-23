class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if my_dict.get(i) is None:
                my_dict[i] = 0
            
            my_dict[i] += 1

        new_dict = dict(sorted(my_dict.items(), key = lambda x: x[1], reverse = True))
        count = 0
        top_k = []
        for i, cnt in new_dict.items():
            top_k.append(i)
            count += 1
            if count == k:
                break

        return top_k
