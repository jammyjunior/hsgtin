a, b = map(int, input().split())
i = 0
while True:
	if a*2!=b:
		i+=1
		a+=1
		b+=1
	else:
		print(i)
		break
