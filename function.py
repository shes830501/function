x = int(input('請輸入西元年份:'))
def is_leap(x):
	if x % 4 != 0:
		return '平年'
	elif x % 4 == 0 and x % 100 != 0:
		return '閏年'
	elif x % 100 == 0 and x % 400 != 0:
		return '平年'
	elif x % 400 == 0 and x % 3200 != 0:
		return '閏年'
print(is_leap(x))
