class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        count = 0

        for i in range(1, len(piles) - (len(piles) // 3), 2):
            count += piles[i]
            
        return count