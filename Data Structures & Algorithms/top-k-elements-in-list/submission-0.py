class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1
        top_k = sorted(freq.items(), key=lambda x:x[1], reverse=True)[:k]
        return [num for num, count in top_k]
        
        

            
            