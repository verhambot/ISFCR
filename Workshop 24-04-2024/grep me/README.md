# grep me


<br/>


## Challenge Description :

Connect to : `nc 35.244.42.91 1234`


<br/>


## Hint :

I like plumbing.


<br/>


## Flag :

`isfcr{$uc3ssfully_Gr3p3d}`


<br/>


## Solution :

- Looking at the challenge name, we know to use the `grep` command.
- Also, by using the hint, we realize that we should use Unix pipes ( ` | ` ).
- Connect to the server and search for `isfcr` string in the output to get the flag : `nc 35.244.42.91 1234 | grep 'isfcr'`

