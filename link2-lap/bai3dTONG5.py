n = int(input())
a = 0
for i in range (1,n*2+2, 2):
	a = a + i/(i+1) 
print(f"{a:.2f}")
