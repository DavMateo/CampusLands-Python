def funcionTest(num1, num2, num3, checked):
    if checked:
        num10 = 10 + num1
        num20 = 20 + num2
        num30 = 30 + num3
    else:
        num10 = False
        num20 = False
        num30 = False
    
    return [num10, num20, num30]


print(funcionTest(1, 2, 3, False))