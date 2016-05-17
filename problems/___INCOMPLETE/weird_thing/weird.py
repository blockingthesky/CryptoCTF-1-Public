import random
import hashlib

def encrypt(msg):
	random.seed(int(hashlib.md5(msg).hexdigest(), 16))
	return "".join([w["c"] for w in sorted([{"c":c,"x":random.random()} for c in msg],key=lambda k:k["x"])])

print encrypt("The quick brown fox jumps over the lazy dog.")
print encrypt("Hello, my name is Magic Mike and I'm here to make you suffer!")
print encrypt("Jacob")
print encrypt("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx redacted xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Output:
#   wreo f qchgruv yoiTb dkap molun zt . xoheejs
#   ai  mnl gm't ueo dkeyrmsu ih oflen!  si yeaMI crfkaea ,MeomeH
#   rueyufotfoTy,mH raiohc_ b_le:soy}hahol diwdks i   i dsgoaivhkaus ,ehest nl{gsguo  _ahtoflsni u_oltetpngosbrsg n clure'ne _rd ' wiwo idpn .oly Grhhe .ur   e ty sategmoo exe!I