class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_freq = 0
        best = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            max_freq = max(max_freq, counts[char])

            window_size = right - left + 1

            while window_size - max_freq > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
                window_size = right - left + 1

            best = max(best, window_size)

        return best