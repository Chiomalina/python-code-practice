from sqlalchemy.sql.functions import next_value


class Solution:
	def romanToInt(self, s:str) -> int:
		roman_values = {
			"I" : 1,
			"V" : 5,
			"X" : 10,
			"L" : 50,
			"C" : 100,
			"D" : 500,
			"M" : 1000
		}

		total = 0

		for i in range(len(s)):
			current_value = roman_values[s[i]]
			next_value = i + 1

			if next_value < len(s) and current_value < roman_values[s[i + 1]]:
				total -= current_value
			else:
				total += current_value

		return total

solution = Solution()
s1 = "MCMXCIV"
s2 = "LVIII"
result_1 = solution.romanToInt(s1)
result_2 = solution.romanToInt(s2)

print(result_1)
print(result_2)