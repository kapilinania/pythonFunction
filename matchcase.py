a= int(input("Enter Your Case Range="))
match a:
    case 1:
        print("this is case one")
    case 2:
        print("this is case two")
    case 3:
        print("this is case three")
    case _:
        print("Default case")

b=int(input("Enter Your Number"))
match b:
    case 1:
        print("this is one")
    case 2:
        print("this is case 2")
    case 3:
        print("this is case 3 ")
    case _:
        print("Default case")