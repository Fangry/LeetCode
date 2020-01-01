# understanding the wording of the question is the hardest part
def dynamicArray(n, queries):    
    seq = [[] for i in range(n)]
    last_ans = 0
    res = []

    for q in queries:
        index = (q[1] ^ last_ans) % n
        
        if q[0] == 1:
            seq[index].append(q[2])
        else:
            position = q[2] % len(seq[index])
            last_ans = seq[index][position]
            res.append(last_ans)
    return res