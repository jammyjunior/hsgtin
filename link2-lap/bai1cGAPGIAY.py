x, y = map(float, input().split())
y=y*1000
i=0
while True:
	x=x*2
	i+=1
	if x>=y:
		print(i)
		break
