import sys
while True:
    print("Type exit to exit")
    response = input().lower()
    if response == "exit":
        break #puedo introducir el comando sys.exit() para terminar el programa
    print("You typed",response,".")