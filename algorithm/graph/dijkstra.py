"""
    过程：
    G = (V, E)， T = ({V0}, {})

    找到T能到达的最近顶点(计算min{dis(v0, u)+w(u, v) | u∈U∧w(u, v)≠∞})并加入T

"""
from data_structure.queue.heap_prio_queue import PrioQueue


def dijkstra(graph, v0):
    v_num = graph.vertex_num()
    assert 0 <= v0 < v_num
    # path[v] = (v', p) 代表v0-v的最短路径前一顶点是v', 该路径长为p
    paths = [None] * v_num
    count = 0
    # 记录V0到各顶点的最短路径
    # cands格式为(p, v, v') 表示v0经v到v'的已知最短路径长为p
    cands = PrioQueue([(0, v0, v0)])
    while count < v_num and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        # 最短路径已知
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        # 挑选出所有vmin的邻接点，将这些顶点及计算后的plen入队
        # 例如v0的邻接点(2, v0, v1), (5, v0, v2)并入队
        # 下次将当前最短距离的v1出队，放入v1的所有邻接边，再下次按plen可能出队v2或其他
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths
