# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：quick_sort 
#   开发人员：LZY 
#   日期：2018-12-27  10:31  
#   开发工具：PyCharm

def quick_sort(list):
    if len(list)<2:
        return list
    else:
        miditem=list[0]
        less=[i for i in list[1:] if i<=miditem]
        great=[i for i in list[1:] if i>miditem]
        return quick_sort(less)+[miditem]+quick_sort(great)

ls=[2,5,7,9,3,4,6]
print(quick_sort(ls))
