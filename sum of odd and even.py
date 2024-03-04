n=int(input("enter a number"))
numbers=range(1,n+1,1)
even_sum=0
odd_sum=0
for num in numbers:
    if (num%2==0):
        print("even",num)
        even_sum +=num
    else:
        print("odd",num)
        odd_sum +=num
        print("sum of the even numbers",even_sum)
        print("sum of the odd numbers", odd_sum)
        
