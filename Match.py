name = input("Enter name: ")

match name:
    case "Louwis" | "Bibeng" | "LA":
        print("Alfred")
    case "Elon":
        print("Musk")
    case "Bill":
        print("Gates")
    case _:
        print("Who?")
            