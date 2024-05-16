import textwrap
def  menu():
    menu = """\n
    =========== MENU ===========    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tlistar conta
    [nu]\tnova usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Valor do depósito:\tR${valor:.2f}"
        print("\n=== Depósido foi realizado com sucesso! ===")
    else:
        print("\n@@@ Erro! Tente novamente.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite
    
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("@@@Operação falhou! Você não tem saldo suficiente.@@@")

    elif excedeu_limite:
        print("@@@Operação falhou! O valor do saque excede o limite.@@@")

    elif excedeu_saques:
        print("@@@Operação falhou! Número máximo de saques excedido.@@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Valor dosaque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("==== Saque relizado com sucesso! ====")

    else:
        print("@@@Operação falhou! O valor informado é inválido.@@@")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato ):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CP (somente número)")
    usuarios = filtrar_usuario(cpf, usuarios)
    if usuarios:
        print("\n@@@ ja Existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o seu nome")
    data_nascimento = input("Informe a sue data de nasimento")
    endereco = input("Informe o endereço (lograduro, rua , bairro)")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== usuario criado com sucesso! ==")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if  usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuario")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== conta cirado com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ usuario não encontrado, flixo de criação de conta encerredo! @@@")

def listar_contas(contas):

    for contas in contas:
        linha = f"""\
        Agêcia:\t{contas["agencia"]}
        c/c:\t\t{contas["numero_conta"]}
        Titular:\t{contas["usuario"]["nome"]}
        """
        print("="*100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAUQES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
  

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAUQES,
            )
            

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario = len(usuarios)

        elif opcao == "nc":
            numero_conta = len(conta) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                conta.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()