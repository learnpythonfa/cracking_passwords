import hashlib
import string
from string import hexdigits

import time

txt = b'hellow'
tic = time.time()
hash_msg = hashlib.md5(txt)
toc = time.time()

alphabet = string.ascii_lowercase
alph = list(alphabet)
print(alph)
tic= time.time()
for i1 in alph:
    for i2 in alph:
        print(i1+i2)
        for i3 in alph:
            for i4 in alph:
                for i5 in alph:
                    for i6 in alph:
                        txt_test = i1+i2+i3+i4+i5+i6
                        # print(txt_test)
                        if hashlib.md5(txt_test.encode('utf-8')).hexdigest() == hash_msg.hexdigest():
                            print(txt_test,'time:',time.time()-tic)
                            exit()

