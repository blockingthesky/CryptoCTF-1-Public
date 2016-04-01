# FLAG{REAL_COFFEE_IS_SO_LEET}
# f1a6{43a1_c0ffee_15_50_1337}
# F1A6{43A1_C0FFEE_15_50_1337}

def proc(k):
    try:
        return int(k, 16)
    except:
        return k

flag = ['F1','A6','{','43','A1','_','C0','FF','EE','_','15','_','50','_','13','37','}']
print ' '.join(str(proc(m)) for m in flag)
