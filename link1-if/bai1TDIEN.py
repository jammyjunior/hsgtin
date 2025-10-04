a = int(input())
if a<=60:
    print(a*1000)
elif a<=120:
    print(60*1000+(a-60)*1200)
elif a<= 200:
    print(60*1000+60*1200+(a-120)*2000)
