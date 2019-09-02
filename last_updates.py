#! /usr/bin/python3

from sh import tail

for line in tail("-5", "/var/log/apt/history.log", _iter=True):
    print(line)