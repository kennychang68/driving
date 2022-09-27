country = input("please input your country : ")
age = input("please input your age : ")
age = float(age)
if country == 'taiwan':
	if age >= 18:
		print("you can go for driving exam")
	else:
		print("you still too young to have the exam")
elif country == 'USA':
	if age >= 16:
		print('you can go for driving exam')
	else:
		print('you still too young to have exam')

else:
	print('please only for taiwan or USA')
