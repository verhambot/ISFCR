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

# Solution 


Given in the challenge is an encrypted image `enc.png` and a program `encrypt.py` that has been used to encrypt the image 

On downloading the files, we see that the image can not be opened and the given code looks very unreadable 

### Given program 
``` py
#El3CTR0N
def frfrrfrafrafrafrafrafarf(asdadasdasdasd):
    while True:
        for item in asdadasdasdasd:
            yield item
jhljkhjklhjkhajsdfhajshd= open('rev.png','rb').read()
asdadasdasdasd=[jhljkhjklhjkhajsdfhajshd[i] for i in range(7)]
jkljkjlkjlkjlkjlkjljl= bytearray([i^j for i,j in zip(jhljkhjklhjkhajsdfhajshd,frfrrfrafrafrafrafrafarf(asdadasdasdasd))])
open("enc.png","wb").write(jkljkjlkjlkjlkjlkjljl)


```

### On changing the variable names and the function name
```py
def cyc(key):
    while True:
        for item in key:
            yield item
f= open('rev.png','rb').read() #opening the image and reading the bytes 
key=[f[i] for i in range(7)] #making a list of the first 7 bytes (key)
enc= bytearray([i^j for i,j in zip(f,cyc(key))]) #XORing each byte with the key
open("enc.png","wb").write(enc)

```
Now we can see that the code takes a png image and reads it as a bytearray assigns the first 7 bytes of the array as the key and then XORs each byte with the first 7 bytes(key)

To decrypt the image we simply read the given image as a bytearray and XOR each byte with the key.

Note: The key has to be same for both the cases therefore we take the first 7 bytes of any other .png image
<br>

# Decrypt.py
```py
from itertools import cycle
f= open('El3CTR0N.png','rb').read() #any random png image just to get the headder 
k=open('enc.png','rb').read() # given encrypted PNG image
key=[f[i] for i in range(7)] # the header of a PNG image
enc= bytearray([i^j for i,j in zip(k,cycle(key))])
open("dec.png","wb").write(enc)
```


