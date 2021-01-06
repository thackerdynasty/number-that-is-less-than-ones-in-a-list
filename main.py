numbers = [5,10,50,100]
user_num = input(int('Give a number.'))
if user_num < 5:
	print('less than 5')
	print('less than 10')
	print('less than 50')
	print('less than 100') 
elif user_num < 10:
	print('less than 10')
	print('less than 50')
	print('less than 100') 
elif user_num < 50:
	print('less than 50')
	print('less than 100')
elif user_num < 100:
	print('less than 100')
else:
	print('not less than anything in the list')
