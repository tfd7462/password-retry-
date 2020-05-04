password = "a123456"
x = 1
y = 2
while x < 4:
	coding = input("請輸入密碼:")
	if coding == password:
		print("登入成功")
		break
	elif coding != password:
		if y < 3 and y > 0:
			print("密碼錯誤剩",y,"次機會")
		elif y ==0:
			print("密碼錯誤，不給你登入了")
			break
	x = x + 1 
	y = y - 1