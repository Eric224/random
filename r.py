import random
r = random.randint(1,100)
t = 0
while t >= 0:
	t = t + 1
	print('第', t, '次猜數字')
	num = input('請猜數字： ')
	num = int(num)
	if num == r:
		print('終於猜對了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
