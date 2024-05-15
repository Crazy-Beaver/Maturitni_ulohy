fronta = []

print("commands: add x, remove, exit")
while True:
    command = input().split(" ")
    match command[0]:
        case "add":
            fronta.append(command[1])
            print(fronta)
        case "remove":
            fronta.pop(0)
            print(fronta)
        case "exit":
            print(fronta)
            break

