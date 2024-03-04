n=1234567
sum=0
for i in str(n):
    sum+=n%10
    n//=10
    print(sum)
