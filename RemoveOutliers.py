# 定義一個可去除n個最大值/最小值的function.
def RemoveOutliers(NumList,n):
    """Remove the n largest numbers and the n smallest numbers."""
    NumList.sort()
    newNumList = NumList[n:-n]
    outliers = NumList[:n] + NumList[-n:]
    return newNumList, outliers

a_list = []
n = int(input("Enter the number of smallest and largest values to remove: "))
s = input("Enter an integer (q or Q to quit): ")
while (s != 'Q' and s != 'q'):
    a_list.append(int(s))
    s = input("Enter an integer (q or Q to quit): ")
newNumList, outliers = RemoveOutliers(a_list,n)
if n * 2 > len(a_list):         # 若使用者輸入的n值超過list長度
    print("Please enter more numbers.")
else:
    print("The original data:", a_list)
    print("The data with the outliers removed: ",newNumList)
    print("The outlier: ", outliers)