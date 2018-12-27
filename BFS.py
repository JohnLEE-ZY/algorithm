# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：BFS 
#   开发人员：LZY 
#   日期：2018-12-27  12:25  
#   开发工具：PyCharm
from collections import deque

def BFS_search(name,graph):
    search_que=deque()
    search_que+=graph[name]
    searched=[]
    while search_que:
        person=search_que.popleft()
        if person not in searched:
            if person_is_sell(person):
                return person
            else:
                search_que += graph[person]
                searched.append(person)
    return False

def person_is_sell(name):
    return  name[-1]=='m'


