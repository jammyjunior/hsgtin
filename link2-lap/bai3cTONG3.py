n = int(input())
a = 0
b = 0
for i in range (1, n+1):
	a = a + 1/(i*(i+1))
for j in range (1, n+1):
	b = b + j/(j+1)
print(f"S1 = {a:.2f}")
print(f"S2 = {b:.2f}")
