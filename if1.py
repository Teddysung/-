age = input('請問你幾歲: ')
age = int(age)
if age >= 20:
	print('你可以辦信用卡')
else:
	print('哈哈你不行, 再等', 20 - age, '年吧你!')