def reverse(number):
    test_num = 0
    while (number > 0):
        remainder = number % 10                  # 餘數
        test_num = (test_num * 10) + remainder   # 將餘數變為第一位後繼續
        number = number // 10                    # 將number處理後進入下一次迴圈
    print(test_num)

num = int(input("Enter an integer: "))           # 缺點:目前無法reverse負數
reverse(num)

#
# 另一種作法:轉換為string
# 若要使用可移除#字號
#

# number = int(input("Enter an integer: " ))

# 主要將數字轉為字串，使用":"來決定其倒轉次序
# 若為負數，先將數字轉為字串並將負號獨立出來

#if (number < 0):
#    print(str(number)[0], end = "")
#    print(str(number)[:0:-1])
#else:
#    print(str(number)[::-1])