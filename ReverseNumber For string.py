number = int(input("Enter an integer: " ))

# 主要將數字轉為字串，使用":"來決定其倒轉次序
# 若為負數，先將數字轉為字串並將負號獨立出來

if (number < 0):
    print(str(number)[0], end = "")
    print(str(number)[:0:-1])
else:
    print(str(number)[::-1])