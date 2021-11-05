n1=int(input('enter the number'))
n2=int(input('enter the second number'))
if  n1>n2:
	lcm=n1
else:
	lcm=n2
while -1:
 	if lcm%n1==0 and lcm%n2==0:
 		break
 	else:
 		lcm=lcm+1
print(lcm)
		