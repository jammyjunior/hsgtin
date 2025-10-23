
n = int(input())
a = 0
b = 0
for i in range (1, n+1):
	a = a + 1/i
for j in range (1, 2*n+2, 2):
	b = b + 1/j
print(f"S1 = {a :.2f}")
print(f"S2 = {b :.2f}") 
