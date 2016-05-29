mx = 1000

def adjmatr(graph):
    ret = [[0] * mx for i in range(mx)]
    for i in range(mx):
        queue = [i]
        ret[i][i] = 1
        visited = [0] * mx
        visited[i] = 1
        while len(queue) != 0:
            while len(queue) != 0:
                cur = queue.pop(0)
                for j in range(mx):
                    if graph[cur][j] and not visited[j]:
                        queue.append(j)
                        visited[j] = 1
                        ret[i][j] = 1
    return ret

pairs = [[int(y) - 1 for y in f.split()] for f in open('graph.dat', 'r').readlines()]
g = [[0] * mx for i in range(mx)]
for pair in pairs:
    g[pair[0]][pair[1]] = 1
adj = adjmatr(g)

queries = [[int(y) - 1 for y in f.split()] for f in open('queries.txt', 'r').readlines()]

bits = ''
for t in queries:
    if adj[t[0]][t[1]]:
        bits += '1'
    else:
        bits += '0'
        

flag = ''
for i in range(len(bits)/8):
    flag += chr(int(bits[8*i:8*(i+1)],2))
print flag
