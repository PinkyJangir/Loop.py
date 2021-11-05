i=int(input('entder the number'))
rev=0
x=i
while i>0:
	rev=rev*10+i%10
	i=i//10
if x==rev:
	print('yes it is palimdrom')
else:
	print('not plimdrom')