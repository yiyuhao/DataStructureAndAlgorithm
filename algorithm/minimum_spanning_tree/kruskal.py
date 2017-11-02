"""
    kruskal算法求最小生成树

    过程：
    G = (V, E)
    取其孤立子图 T = (V, {})
    由小到大取E，加入T (重要：如果加入后连通分量未减少1，则抛弃该边)。

    判断连通分量的解决方案：为每个连通分量确定一个代表元rep，如果两个顶点的代表元相同，则他们连通
"""


def kruskal(graph):
    """

    :param graph: 图G，需要具有property或函数G.vertex_num，与函数G.out_edges(vi)求顶点的所有邻接边
    :return:
    """
    # 获取G的边数
    v_num = graph.vertex_num
    # 代表元list，每个元素对应每个顶点的代表元
    reps = [i for i in range(v_num)]
    rv, edges = [], []

    for i in range(v_num):
        # 获取V0, V1, ... 的邻接边
        for vertex, weight in graph.out_edges(i):
            edges.append((weight, i, vertex))

    # 按权低到高排序 O(nlogn)
    edges.sort()

    # vi vi对应两条边
    for w, vi, vj in edges:
        # 属于不同连通分量
        if reps[vi] != reps[vj]:
            # 记录这条边
            rv.append((vi, vj), w)
            # 生成了n-1条边，构造生成树完成
            if len(rv) == v_num - 1:
                break

            # 构造一条边后，合并了连通分量，设置这表边的代表元
            rep, orep = reps[vi], reps[vj]
            for i in range(v_num):
                if reps[i] == orep:
                    reps[i] = rep
    return rv
