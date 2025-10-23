a = int(input())
i=0
while a!=0:
	if a%2==1:
		a=a-1
	else:
		a=a//2
	i+=1
print(i)
