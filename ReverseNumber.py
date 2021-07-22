def reverse(number):
    test_num = 0
    while (number > 0):
        remainder = number % 10                  # 餘數
        test_num = (test_num * 10) + remainder   # 將餘數變為第一位後繼續
        number = number // 10                    # 將number處理後進入下一次迴圈
    print(test_num)

num = int(input("Enter an integer: "))
reverse(num)