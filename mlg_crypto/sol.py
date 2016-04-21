inp = open('mlg_crypto.txt', 'r')
inp.readline()
dt = {'BREAK':' '}
assign = list('abcdefghijklmnopqrstuvwxyz')
st = ''
for m in inp.readlines()[:-1]:
    m = m.strip().split("_")
    for k in m:
        if dt.has_key(k):
            st += dt.get(k)
        else:
            p = assign.pop()
            dt.update({k:p})
            st += dt.get(k)

print st
