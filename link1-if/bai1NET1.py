a = int(input())
if a<=60:
    print(a*80)
elif a<=120:
    print(60*80+(a-60)*50)
else:
    print(60*80+60*50+(a-120)*30)