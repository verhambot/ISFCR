# REVpy-v1


<br/>


## Challenge Description :

rev them brain muscles harder.


<br/>


## Hint :

Characters might be jumbled when you print the flag.


<br/>


## Flag :

`isfcr{harder_python_rev}`


<br/>


## Solution :

- On going through `chall.py`, we notice 2 things :
    1. The length of the flag is even.
    2. The flag contains only lowercase alphabets and `{`, `}`, `!`, and `_`.

- Since every pair of characters is multiplied, we cycle through our allowed ASCII values and check if they are factors.

- The factors, and consequently the characters, that we get might be jumbled and must be re-arranged (hence the hint).

- On running `solve.py`, we get the output :
    ```
    i s
    c f
    r {
    a h
    d r
    e r
    p _
    t y
    h o
    n _
    e r
    v }
    ```

- On re-arranging the jumbled output, we get the flag.
