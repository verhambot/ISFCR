# REVpy-v0


<br/>


## Challenge Description :

rev them brain muscles.


<br/>


## Flag :

`isfcr{f1r57_py7h0n_r3v}`


## Solution :

- On examining `chall.py`, we see that every even index gets added with 1 while every odd index gets subtracted with 1.
    ```py
    from flag import flag

    output_flag = ''

    for index, character in enumerate(flag):
        if index % 2 == 0:
            output_flag += chr(ord(character) + 1)
    else:
        output_flag += chr(ord(character) - 1)

    with open('output.txt', 'w') as file:
        file.write(output_flag)

    ```


- To get the flag, just perform the reverse operation (subtract 1 at even index and add 1 at odd index).
    ```py
    with open('output.txt', 'r') as file:
        content = file.read()

    flag = ''

    for index, character in enumerate(content):
        if index % 2 == 0:
            flag += chr(ord(character) - 1)
        else:
            flag += chr(ord(character) + 1)

    print(flag)

    ```
