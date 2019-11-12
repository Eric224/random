import random
x_min = input('請輸入最小值： ')
y_max = input('請輸入最大值： ')
x_min = int(x_min)
y_max = int(y_max)
r = random.randint(x_min, y_max)
t = 0
while t >= 0:
	t = t + 1
	num = input('請猜數字： ')
	num = int(num)
	if num == r:
		print('終於猜對了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('你已經猜了', t, '次')
