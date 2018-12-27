# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：factorial 
#   开发人员：LZY 
#   日期：2018-12-27  9:07  
#   开发工具：PyCharm
def factorial(item):
    if item==1:
        return item
    else:
        return item*factorial(item-1)


print(factorial(5))
