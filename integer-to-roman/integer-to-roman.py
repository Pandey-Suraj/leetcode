class Solution:
	def intToRoman(self, x: int) -> str:

		ans = ''
		data = {'1000': ['M', 'G', 'K'], '100': ['C', 'D', 'M'], 
				'10': ['X', 'L', 'C'], '1': ['I', 'V', 'X']}
		for base, alpha in data.items():
			base = int(base)
			y = x // base
			x = x % base

			roman = ''
			if y == 0:
				pass
			elif 1 <= y <= 3:
				roman = alpha[0]*y
			elif y == 4:
				roman =  alpha[0] + alpha[1]
			elif 5 <= y <= 8:
				roman =  alpha[1] + alpha[0]*(y-5)
			elif y == 9:
				roman = alpha[0] + alpha[2]
			ans = ans + roman

			# print(y, x)
		return (ans)