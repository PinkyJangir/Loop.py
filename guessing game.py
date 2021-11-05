num=10
chance=5
i=1
while i<=5:
	guess=int(input('enter the numner'))
	if guess<num:
		print('chhota hai')
	elif guess>num:
		print('bda h')
	elif guess==num:
		print('sahi h')
		break
	i=i+1
if i==6:
	print("you l0st your  hance")