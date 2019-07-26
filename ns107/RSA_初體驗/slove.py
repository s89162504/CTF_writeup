from Crypto.Util.number import *
import gmpy2

# C = pow(M, e, N)
# M = pow(C, d, N)

e = 65537
N = 1294506718235478161592096722917508216492977651068363875076991157611

#from factordb.com

p = 1073272790751895298208115032919109
q = 1206130192985321597931861298372079

phi_n = (p-1)*(q-1)
d = inverse(e, phi_n)

C = 26391362288757932254855463314223757853307296781294155211094052683
m = pow(C, d, N)

print long_to_bytes(m)