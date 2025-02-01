class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}

        total = 0
        prev = 0

        for x in s:
            current_val = roman_to_int[x]
            if current_val > prev:
                total = total + current_val - 2*prev

            else:
                total += current_val

            prev = current_val
        return total
