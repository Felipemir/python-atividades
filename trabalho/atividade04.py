# EXIGÊNCIA DE CÓDIGO 1: Nome completo
print("Bem-vindos ao sistema do robson felipe da silva miranda")

# EXIGÊNCIA DE CÓDIGO 2: Lista de funcionários e ID global (RU)
lista_funcionarios = []
id_global = 4690823

# EXIGÊNCIA DE CÓDIGO 3: Função para cadastrar funcionário
def cadastrar_funcionario(id):
    funcionario = {
        'id': id,
        'nome': input("Nome: "),
        'setor': input("Setor: "),
        'salario': float(input("Salário: "))
    }
    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!")

# EXIGÊNCIA DE CÓDIGO 4: Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")

        
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                for func in lista_funcionarios:
                    print(func)
            elif opcao == 2:
                id_consulta = int(input("Informe o ID: "))
                for func in lista_funcionarios:
                    if func['id'] == id_consulta:
                        print(func)
                        break
                else:
                    print("ID não encontrado.")
            elif opcao == 3:
                # Implementação para consulta por setor
                pass
            elif opcao == 4:
                break  # Sair do loop e retornar ao menu
            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")
 

# EXIGÊNCIA DE CÓDIGO 5: Função para remover funcionário
def remover_funcionario():
    while True:
        id_remover = int(input("Informe o ID do funcionário a ser removido: "))
        for i, func in enumerate(lista_funcionarios):
            if func['id'] == id_remover:
                del lista_funcionarios[i]
                print("Funcionário removido com sucesso!")
                return
        else:
            print("ID inválido.")

# EXIGÊNCIA DE CÓDIGO 6: Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == '2':
        consultar_funcionarios()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")
