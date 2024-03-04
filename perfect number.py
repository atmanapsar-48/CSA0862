n =eval(input("enter the number"))
sum_divisors = sum([i for i in range(1, n) if n % i == 0])
is_perfect = n == sum_divisors

if is_perfect:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
