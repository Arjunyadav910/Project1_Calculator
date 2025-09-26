A=int(input("Enter the value of A--->"))
B=int(input("Enter the value of B--->"))
operations=str(input("Enter the operator you want to use--->"))
match operations:
    case "+":
        print("Addition of A and B is--->"A+B)
    case "-":
        print("Subtraction of A and B is--->"A-B)
    case "*":
        print("Multiplication of A and B is--->"A*B)
    case "/":
        print("Division of A and B is--->"A/B)
    case "%":
        print("Modulus of A and B is--->"A%B)
    case "=":
        print("Equal of A and B is--->"A==B)
    case _:
        print("Invalid operator used--->")
