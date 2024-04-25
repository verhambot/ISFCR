# segfault


## Challenge Description :

There are two kinds of programmers. Those who understand pointers and segmentation faults.

Connect to : `nc 35.244.42.91 2560`


<br/>


## Flag :

`isfcr{l00ks_lik3_y0u_lik3_wr1ting_segf4ult-y_c0d3}`


<br/>


## Solution :

1. Connect to server using the given command : `nc 35.244.42.91 2560`
2. Enter a very long string to cause a segmentation fault and print the flag.
    - You might want to use Python to generate the long string : `python -c "print(3000 * 'A')"`
    - The segmentation fault occurs due to fact that the program tries to copy this large string into a smaller string.
    - The segfault handler prints the flag.
