# not enough moni

<br/>

## Challenge Description :
infinite money glitch?

<br/>

## Flag :
`isfcr{v4lu3_und3rfl0w}`

<br/>

## Solution :

There are two intended ways to solve this challenge :

### 1. Value Underflow
1. Run `moni.exe` : `./moni.exe`
2. Buy `[3] Solution: 250 hackcoins` 6 times. You will notice that your `balance` will increase to `4294967133 hackcoins`.
    - This is due to a behaviour called `value underflow`.
    - When an `unsigned` data type is used, it's minimum value is `0`.
    - If the `unsigned` data type is decremented below it's minimum value, it wraps around to the maximum possible value for that data type.
3. Now, you have enough `balance` to buy `[2] Flag: 31337 hackcoins` and get the flag.

### 2. Ghidra
1. Decompile `moni.exe` using Ghidra.
2. In the `Functions` menu, under `Symbol Tree`, find the `generate_flag` function.
3. Convert the `ascii`/`hex` values into `char` values and you should see the flag.
