num=int(input('enter the number'))
sum=0
temp=num
while temp>0:
	f=1
	i=1
	rem=temp%10
	while i<=rem:
		f=f*i
		i=i+1
	sum=sum+f
	temp=temp//10
if sum==num:
	print('yes it is strong number',num)
else:
	print('not strong')