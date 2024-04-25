#!/usr/bin/python3

import sys
import subprocess

def main():
    print("Enter python commands to run:", flush = True)
    line = input()
    try:
        result = subprocess.run([sys.executable, "-c", line], timeout=1, check=True, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired as e:
        print("Timed out\nExiting...", flush = True)
        exit(1)
    except subprocess.CalledProcessError as e:
        print("Invalid input\nExiting", flush = True)
        exit(1)

if __name__ == "__main__":
    main()
