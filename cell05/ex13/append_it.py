import sys

params = sys.argv[1:]

if not params:
    print("none")
else:
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")