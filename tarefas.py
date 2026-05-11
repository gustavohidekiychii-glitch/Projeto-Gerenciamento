tarefas = []

def cadastrar_tarefa():
    print('\n=== CADASTRAR NOVA TAREFA ===')
    descricao = input('Descrição da tarefa: ')
    vencimento = input('Data de vencimento (dd/mm/aaaa): ')
    
    # status inicial sempre "pendente"
    tarefa = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'vencimento': vencimento,
        'status': 'pendente'
    }
    
    tarefas.append(tarefa)
    print('Tarefa cadastrada com sucesso!')

def listar_tarefas():
    print('\n=== LISTAGEM DE TAREFAS ===')
    
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
        return
    
    print('1 - Listar todas')
    print('2 - Filtrar por status')
    print('3 - Filtrar por data de vencimento')
    opcao = input('Escolha uma opção: ')
    
    if opcao == "1":
        mostrar_todas_tarefas()
    elif opcao == "2":
        filtrar_por_status()
    elif opcao == "3":
        filtrar_por_data()
    else:
        print("Opção inválida!")
 
    
def mostrar_todas_tarefas():
    print('==Tarefas==')
    for tarefa in tarefas:
        print(f'ID: {tarefa["id"]}')
        print(f'Descrição: {tarefa["descricao"]}')
        print(f'Vencimento: {tarefa["vencimento"]}')
        print(f'Status: {tarefa["status"]}')
        print('-------------------')

def filtrar_por_status():
    print("\nFiltrar por status:")
    print('1 - Pendente')
    print('2 - Em andamento')
    print('3 - Concluída')

    opcao = int(input('Escolha o status: '))

    if opcao == 1:
        status_filtro = 'pendente'
    elif opcao == 2:
        status_filtro = 'em andamento'
    elif opcao == 3:
        status_filtro = 'concluída'
    else:
        print("Opção inválida.")
        return

    tarefas_filtradas = []

    for tarefa in tarefas:
        if tarefa['status'] == status_filtro:
            tarefas_filtradas.append(tarefa)

    if len(tarefas_filtradas) == 0:
        print(f"\nNenhuma tarefa com status '{status_filtro}'.")
        return

    print(f'\n--- TAREFAS COM STATUS: {status_filtro} ---')

    for tarefa in tarefas_filtradas:
        print(f'ID: {tarefa["id"]}')
        print(f'Descrição: {tarefa["descricao"]}')
        print(f'Vencimento: {tarefa["vencimento"]}')
        print(f'Status: {tarefa["status"]}')
        print('-------------------')

def filtrar_por_data():
    data_busca = input("\nDigite a data de vencimento (dd/mm/aaaa): ")