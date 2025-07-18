class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        window_size = n - k
        
        # If k == n, take all cards
        if window_size == 0:
            return total
        
        # Find the minimum sum of a window of size n - k
        window_sum = sum(cardPoints[:window_size])
        min_window_sum = window_sum

        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, window_sum)

        return total - min_window_sum