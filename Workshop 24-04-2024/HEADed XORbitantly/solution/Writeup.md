# HEADed XORbitantly
<br>

## Challenge Description

Someone has messed with an image containing important information I think they used this program to do so

<br>

## Hints 

### Hint 1
    A^B=C
    A=C^B
### Hint 2
    Look up file headers for PNGs.
    
<br>

# Flag: *_isfcr(x0r_r3v)_*

<br>

# Soultion 

<br>

## Given 

Given in the challenge is an encrypted image `enc.pn` and an program `ecrypt.py` that has been used to encrypt the image 

On downloading the files we see that the image can not be opened and the given code looks very unreadable 

### Given program 
``` py
def frfrrfrafrafrafrafrafarf(asdadasdasdasd):
    while True:
        for item in asdadasdasdasd:
            yield item
jhljkhjklhjkhajsdfhajshd= open('rev.png','rb').read()
asdadasdasdasd=[jhljkhjklhjkhajsdfhajshd[i] for i in range(7)]
jkljkjlkjlkjlkjlkjljl= bytearray([i^j for i,j in zip(jhljkhjklhjkhajsdfhajshd,frfrrfrafrafrafrafrafarf(asdadasdasdasd))])
open("enc.png","wb").write(jkljkjlkjlkjlkjlkjljl)


```

### on changing the variable names and the function name
```py
def cyc(key):
    while True:
        for item in key:
            yield item
f= open('rev.png','rb').read()
key=[f[i] for i in range(7)]
enc= bytearray([i^j for i,j in zip(f,cyc(key))])
open("enc.png","wb").write(enc)

```
Now in the new code with variable names changed we see that an image is being opend and then xored with the headder of an png file 

We find out that the key is the header 

On Xoring the bytearray of the given image with the first 7 bytes of anyother .png file we get the image and the flag

<br>

```py
from itertools import cycle
f= open('anypng.png','rb').read() #any random png image just to get the headder 
k=open('enc.png','rb').read() # given encrypted PNG image
key=[f[i] for i in range(7)] # the header of a PNG image
enc= bytearray([i^j for i,j in zip(k,cycle(key))])
open("dec.png","wb").write(enc)
```


