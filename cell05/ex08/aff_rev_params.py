import sys

params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    for param in reversed(params):
        print(param)