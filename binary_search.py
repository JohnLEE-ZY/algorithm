# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：binary_search 
#   开发人员：LZY 
#   日期：2018-12-27  8:36  
#   开发工具：PyCharm
def binary_search(list, item):
    high = len(list) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        if guess==item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

ls=[1,3,4,5,7,8,9,12,18]
print(binary_search(ls,9))