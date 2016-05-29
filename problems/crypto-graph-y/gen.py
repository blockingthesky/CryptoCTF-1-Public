import random

mx = 1000

def gen_graph():
    edges = 2000
    ret = [[0] * mx for i in range(mx)]
    rstr = ''
    for i in range(edges):
        a = random.randint(1,mx)
        b = random.randint(1,mx)
        if a == b:
            continue
        rstr += str(a) + ' ' + str(b) + '\n'
        ret[a-1][b-1] = 1
    return ret, rstr

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

g, s = gen_graph()
open('graph.dat', 'w').write(s)
adj = adjmatr(g)

validpairs = []
invalidpairs = []
for i in range(mx):
    for j in range(mx):
        if adj[i][j]:
            validpairs.append((str(i+1),str(j+1)))
        else:
            invalidpairs.append((str(i+1),str(j+1)))

message = 'Graph theory, graph theory. A cool field, right? I wonder what sorts of asymmetric cryptosystems could exist with some good old graph theory. flag{who_knew_nodes_and_edges_could_be_so_cool}'
bits = ''.join(bin(ord(t))[2:].zfill(8) for t in message)
out = open('queries.txt', 'w')
for bit in bits:
    if bit == '1':
        f = random.choice(validpairs)
    else:
        f = random.choice(invalidpairs)
    out.write(str(f[0] + ' ' + f[1] + '\n'))
out.close()
