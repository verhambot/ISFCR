#!/bin/sh

gcc segfault.c -o segfault -Wall -z relro -z now -fno-stack-protector
