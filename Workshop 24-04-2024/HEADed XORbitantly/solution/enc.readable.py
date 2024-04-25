def cyc(key):
    while True:
        for item in key:
            yield item
f= open('rev.png','rb').read() #opening the image and reading the bytes 
key=[f[i] for i in range(7)] #making a list of the first 7 bytes (key)
enc= bytearray([i^j for i,j in zip(f,cyc(key))]) #XORing each byte with the key
open("enc.png","wb").write(enc)
