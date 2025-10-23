a = input()
for i in range(len(a)):
	j = -i-1
	if a[i]!=a[j]:
		print(0)
		break
else:
	print(1)
