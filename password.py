userpassword = input('請輸入密碼: ')
times = 3
while True:
	if userpassword == 'a123456':
		print('登入成功!')
		break
	else:
		times = times-1
		if times > 0:
			print('密碼錯誤! 還有', times, '次機會!')
			userpassword = input('請輸入密碼: ')
		else:
			print('密碼錯誤三次，已被鎖定')
			break