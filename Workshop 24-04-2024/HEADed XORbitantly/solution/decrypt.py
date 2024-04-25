from itertools import cycle
f= open('El3CTR0N.png','rb').read() #any random png image just to get the headder 
k=open('enc.png','rb').read() # given encrypted PNG image
key=[f[i] for i in range(7)] # the header of a PNG image
enc= bytearray([i^j for i,j in zip(k,cycle(key))])
open("dec.png","wb").write(enc)
