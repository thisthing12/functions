def check_factor(bigger_num, smaller_num):
    return bigger_num % smaller_num == 0


big_num = int(input("Enter a number: "))
small_num = int(input("What number do you want to check as a factor: "))
if check_factor(big_num, small_num):
    print(f"{small_num} is a factor of {big_num}")
else:
    print(f"{small_num} is NOT a factor of {big_num}")
