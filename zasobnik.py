zasobnik = []

print("commands: add x, remove, exit")
while True:
    command = input().split(" ")
    match command[0]:
        case "add":
            zasobnik.append(command[1])
            print(zasobnik)
        case "remove":
            zasobnik.pop(-1)
            print(zasobnik)
        case "exit":
            print(zasobnik)
            break

