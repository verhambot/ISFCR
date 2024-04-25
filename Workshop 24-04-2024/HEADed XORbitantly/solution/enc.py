def cyc(key):
    while True:
        for item in key:
            yield item
f= open('xor_chall_header\deployfiles\\rev.png','rb').read()
key=[f[i] for i in range(7)]
enc= bytearray([i^j for i,j in zip(f,cyc(key))])
open("enc.png","wb").write(enc)