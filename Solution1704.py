class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        half = int(n/2)
        first_half = s[:half]
        second_half = s[half:]
        vowels = 'UEOAIueoai'
        return sum(1 for c in first_half if c in vowels) == sum(1 for c in second_half if c in vowels)