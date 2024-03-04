for number in range(1, 1001):
    digits = str(number)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    if armstrong_sum == number:
        print(number)e?
