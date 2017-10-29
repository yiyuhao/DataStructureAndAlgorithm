def gen_pnext(p):
    """KMP算法中，生成针对匹配字符串p中各位置i的下一检查位置表"""

    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]

    return pnext


r = gen_pnext('abbcabcaabbcaa')
pass
