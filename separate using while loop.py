num=eval(input("enter a num :"))
num1=num
sum=0
while(num>0):
    if ((num%10)%2!=0):
        sum+=num%10
    num=num//10
print("sum",sum)
