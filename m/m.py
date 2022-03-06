from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())

    # Adj list
    n1 = {}
    for _ in range(n-1):
        a, b = map(int, input().split(" "))
        s = n1.get(a, set())
        s.add(b)
        n1[a] = s
        s = n1.get(b, set())
        s.add(a)
        n1[b] = s

    # Parents
    parents = {
        1: None
    }
    
    visited = set()
    queue = deque()
    queue.append(1)

    #BFS
    while len(queue) > 0:
        node = queue.pop()
        visited.add(node)
        for neighbor in n1[node]:
            if neighbor not in parents:
                parents[neighbor] = node
            if neighbor not in visited:
                queue.append(neighbor)

    #print(parents)
    
    q = 1
    nxt = int(input())
    prev = 0
    for _ in range(n - 1):
        prev = nxt
        nxt = int(input())
        if q == 0:
            continue

        if parents[prev] == parents[nxt]: #LR
            continue
        if parents[prev] != None:
            p = parents[prev] # parent
            if p == nxt:
                continue
            if parents[p] != None:
                p = parents[p] # gparent
                if p == nxt:
                    continue
                if p == parents[nxt]:
                    continue
                if parents[p] != None:
                    p = parents[p] # ggparent
                    if p == nxt:
                        continue

        if parents[nxt] != None:
            p = parents[nxt] # parent
            if p == prev:
                continue
            if parents[p] != None:
                p = parents[p] # gparent
                if p == prev:
                    continue
                if p == parents[prev]:
                    continue
                if parents[p] != None:
                    p = parents[p] # ggparent
                    if p == prev:
                        continue

        q = 0

    print(q)
