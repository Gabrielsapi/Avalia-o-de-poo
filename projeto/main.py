from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_pupanca import ContaPoupanca
from sistema.banco import Banco


def selecionar_conta(banco: Banco):
    contas = banco.listar_contas()

    if not contas:
        print("Nenhuma conta cadastrada.")
        return None

    for conta in contas:
        print(f"ID: {conta.id} | Cliente: {conta.cliente.nome}")

    try:
        conta_id = int(input("Informe o ID da conta: "))
    except ValueError:
        print("Entrada inválida.")
        return None

    conta = banco.buscar_conta(conta_id)

    if not conta:
        print("Conta não encontrada.")

    return conta


def executar():
    banco = Banco()

    while True:
        print("\nSistema de Caixa Eletrônico")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar saldo")
        print("5 - Histórico")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                tipo = input("Tipo de conta (1 - Corrente | 2 - Poupança): ")

                cliente = Cliente(nome, cpf)

                if tipo == "1":
                    conta = ContaCorrente(cliente)
                elif tipo == "2":
                    conta = ContaPoupanca(cliente)
                else:
                    print("Tipo inválido.")
                    continue

                banco.adicionar_conta(conta)
                print(f"Conta criada com ID {conta.id}")

            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao in ["2", "3", "4", "5"]:
            conta = selecionar_conta(banco)
            if not conta:
                continue

            if opcao == "2":
                try:
                    valor = float(input("Valor do depósito: "))
                    if not conta.depositar(valor):
                        print("Valor inválido.")
                except ValueError:
                    print("Entrada inválida.")

            elif opcao == "3":
                try:
                    valor = float(input("Valor do saque: "))
                    if not conta.sacar(valor):
                        print("Operação não permitida.")
                except ValueError:
                    print("Entrada inválida.")

            elif opcao == "4":
                print(f"Saldo atual: R${conta.saldo:.2f}")

            elif opcao == "5":
                historico = conta.obter_historico()
                if not historico:
                    print("Nenhuma operação registrada.")
                else:
                    for item in historico:
                        print(item)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar()