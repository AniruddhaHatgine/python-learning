milk_type=input("Enter Milk Type: ")

match milk_type:
    case "C":
        print("Cow Milk")
    case "B":
        print("Buffalo Milk")
    case "G":
        print("Goat Milk")
    case _:
        print("Invalid Milk Type")