# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：select_sort 
#   开发人员：LZY 
#   日期：2018-12-27  8:50  
#   开发工具：PyCharm

def find_min(list):
    minitem=list[0]
    minindex=0
    for i in range(1,len(list)):
        if minitem>list[i]:
            minitem=list[i]
            minindex=i
    return minindex

def select_sort(list):
    r_list=[]
    for i in range(0,len(list)):
        minindex=find_min(list)
        r_list.append(list.pop(minindex))
    return r_list

ls=[3,15,2,7,5,9,1,8,6]
print(select_sort(ls))

