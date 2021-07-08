def raise_to_power(base_num, pow_num):
    Result = 1
    for index in range(pow_num):
        Result = Result * base_num
    return Result

print(raise_to_power(22,3))