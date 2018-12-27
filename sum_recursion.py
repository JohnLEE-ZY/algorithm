# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：sum_recursion
#   开发人员：LZY 
#   日期：2018-12-27  9:56  
#   开发工具：PyCharm
def sum_recursion(list):
    if list:
        return list.pop() * sum_recursion(list[0:len(list)])
    else:
        return 1


ls=[1,3,5,7,9]
print(sum_recursion(ls))
