a, b = map(int, input().split())
x = a
while True:
	print(x, end=" ")
	x= x+a
	if x>b:
		print()
		break
