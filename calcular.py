def calcular(op):
    A0=float(input('digite o primeiro valor  '))
    op=input("selecione a operação ")
    B0=float(input('digite o segundo valor  '))
    match op:
        case ("+"):
            print(A0 + B0)
        case ("-"):
            print(A0 - B0)
        case ("x"):
            print(A0 * B0)
        case ("/"):
            print(A0/B0)
            print("obrigafo")
    
calcular()
