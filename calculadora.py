#João Pedro Mendes Nowicki - Matricula: 202308232746.
#Rafael Kahl Konorath - Matricula: 202308232711.
def calculator():
    while True:
        try:
            numero1 = float(input("Insira o primeiro número que deseja fazer a operação: "))
            print("Escolha o tipo de operação que deseja efetuar:")
            print("1: Somar")
            print("2: Subtrair")
            print("3: Dividir")
            print("4: Multiplicar")
            operation = input("Digite o número correspondente à operação que deseja efetuar: ")
            if operation not in ['1', '2', '3', '4']:
                print("Operação inválida. Por favor, tente novamente.")
                continue
            numero2 = float(input("Insira o segundo número: "))
            if operation == '1':
                resultadoFinal = numero1 + numero2
                operation_str = "Soma"
            elif operation == '2':
                resultadoFinal = numero1 - numero2
                operation_str = "Subtração"
            elif operation == '3':
                if numero2 == 0:
                    print("Erro: Divisão por zero não é permitida. Por favor, tente novamente.")
                    continue
                resultadoFinal = numero1 / numero2
                operation_str = "Divisão"
            elif operation == '4':
                resultadoFinal = numero1 * numero2
                operation_str = "Multiplicação"
            print(f"O resultado Finala da {operation_str} entre {numero1} e {numero2} é: {resultadoFinal}")
            CalcularNovamente = input("Deseja realizar outra operação? (s/n): ").lower()
            if CalcularNovamente != 's':
                break
        except ValueError:
            print("ERRO!!!!!. Por favor, insira um numero Real, ou use '.' para separar casas decimais.")
calculator()