n = int(input())
a=0
b=1
c=0
for i in range(1, n+1):
	a+=i
for j in range(1, n+1):
	b = b * j
for k in range(1, n+1):
	c =c + k**2
print(f"S1 = {a}")
print(f"S2 = {b}")
print(f"S3 = {c}")
