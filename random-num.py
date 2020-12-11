import random

r = random.randint(1, 100)
while True:
	num = input('猜猜看幾號?')
	num = int(num)
	if num == r:
		print('恭喜猜中了! ')
		break
	elif num > r:
		print('猜大了! ')
	elif num < r:
		print('猜小了! ')
