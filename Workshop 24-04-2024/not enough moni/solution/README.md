# not enough moni

flag : `isfcr{v4lu3_und3rfl0w}`

There are two intended ways to solve this challenge :

### 1. Value Underflow
1. Download both the `moni.exe` and `moni.c` files. You will see that the flag is redacted from the `moni.c` file.
2. Give executable permissions to the `moni.exe` file : `chmod +x moni.exe`
3. Run `moni.exe` : `./moni.exe`
4. Buy `[3] Solution: 250 hackcoins` 6 times. You will notice that your `balance` will increase to `4294967133 hackcoins`.
    - This is due to a behaviour called `value underflow`.
    - When an `unsigned` data type is used, it's minimum value is `0`.
    - If the `unsigned` data type is decremented below it's minimum value, it wraps around to the maximum possible value for that data type.
5. Now, you have enough `balance` to buy `[2] Flag: 31337 hackcoins` and get the flag.

### 2. Ghidra
1. Open Ghidra, create a new project, import the `moni.exe` file, and analyze it.
2. In the `Functions` menu, under `Symbol Tree`, find the `generate_flag` function.
3. Convert the `hex` values into `char` values and you should see the flag.
