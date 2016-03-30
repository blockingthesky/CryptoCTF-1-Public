import sys

def init(p):
    matrix=[[0]*p for i in range(p)]
    matrix[0]=[1]*2+[0]*(p-2)
    for x in range(1,p-1):
        row = [0]*(x+1)+[1]+(p-x-2)*[0]
        matrix[x]=row
    matrix[p-1]=[1]+[0]*(p-1)
    return matrix
    
def matrix_mult(a,b):
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) % 128 
             for col_b in zip_b] for row_a in a]

if len(sys.argv)!=3:
    raise ValueError("arguments should be [plaintext] [integer key]")

plaintext = sys.argv[1]
N = int(sys.argv[2])
p = len(plaintext)
M = [map(ord, list(plaintext))]
Q = [[0]*i+[1]+[0]*(p-i-1) for i in range(p)]

if N>=1:
    Q = matrix_mult(Q,init(p))
    
for x in range(N-1):
    Q=matrix_mult(Q,Q)

out = open("fibcrypted.txt", "w")
out.write(''.join([chr(x) for x in matrix_mult(M,Q)[0]]))
out.close()