# _*_ code = utf-8 _*_
#   项目名称： project  
#   文件名：Dijkstra 
#   开发人员：LZY 
#   日期：2018-12-27  20:57  
#   开发工具：PyCharm

def dijkstra(graph,src):
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=[]  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}    # 记录源节点到各个节点的距离
    for i in nodes:
         distance[i]=graph[src][i]      # 初始化 #
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        mid_distance=float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=new_distance # 进行距离更新
                    k=d
                    pre=v
        distance[k]=mid_distance # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
        print(visited,nodes) # 输出节点的添加过程
    return distance,path

graph_list = [ [0, 2, 1, 4, 5, 1], [1, 0, 4, 2, 3, 4],
               [2, 1, 0, 1, 2, 4], [3, 5, 2, 0, 3, 3],
               [2, 4, 3, 4, 0, 1], [3, 4, 7, 3, 1, 0]]

distance,path=dijkstra(graph_list,0)
print(distance,path)
