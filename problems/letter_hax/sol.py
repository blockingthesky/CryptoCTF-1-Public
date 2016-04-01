message = '241 166 { 67 161 _ 192 255 238 _ 21 _ 80 _ 19 55 }'.split()
def proc(m):
    try:
        k = int(m)
        return hex(k)[2:]
    except:
        return m

print ''.join(proc(j) for j in message)
