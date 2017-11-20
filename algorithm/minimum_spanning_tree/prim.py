"""
    prim算法求最小生成树

    过程：
    1、G = (V, E),  T = {{}, {}}
    2、取G中一顶点V0加入T， V0的最小邻接边加入T
    3、取G中一顶点在T，另一顶点不在T的最小邻接边加入T(循环执行直至T包含所有G顶点)
"""

from data_structure.queue.heap_prio_queue import PrioQueue


def prim(graph):
    """优先队列cands记录候选边，依次遍历找到满足步骤3的边"""
    v_num = graph.vertex_num
    mst = [None] * v_num
    # 记录候选边(weight, vi, vj)
    cands = PrioQueue([(0, 0, 0)])
    count = 0

    while count < v_num and not cands.is_empty():
        w, vj, vi = cands.dequeue()
        if mst[vi]:
            continue
        mst[vi] = ((vj, vi), w)
        count += 1
        for vi, w in graph.out_edges(vi):
            if not mst[vi]:
                cands.enqueue((w, vi, vi))
    return mst
