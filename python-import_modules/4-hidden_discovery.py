#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    string = dir(hidden_4)
names = sorted ([name for name in string  if not name.startswith ("__")  ])
for name in names:
    print ("{}".format(name))
