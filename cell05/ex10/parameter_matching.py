import sys

if len(sys.argv) !=2:
    print("Nope, sorry...")
else:
    user_input = input("Enter aword: ")
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")    