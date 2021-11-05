n1=int(input('enter the nunber'))
n2=int(input('enter the number'))
while n1%n2!=0:
	rem=n1%n2
	n1=n2
	n2=rem 
print('hcf',rem)